#include "Bitmap.h"

#include <algorithm>
#include <cmath>
#include <fstream>
#include <limits>
#include <stdexcept>

namespace {

std::uint16_t Read16(const std::vector<std::uint8_t>& bytes, std::size_t at) {
    return static_cast<std::uint16_t>(bytes[at] | (std::uint16_t(bytes[at + 1]) << 8));
}

std::uint32_t Read32(const std::vector<std::uint8_t>& bytes, std::size_t at) {
    return std::uint32_t(bytes[at]) | (std::uint32_t(bytes[at + 1]) << 8) |
           (std::uint32_t(bytes[at + 2]) << 16) | (std::uint32_t(bytes[at + 3]) << 24);
}

void Write16(std::vector<std::uint8_t>& bytes, std::size_t at, std::uint16_t value) {
    bytes[at] = static_cast<std::uint8_t>(value);
    bytes[at + 1] = static_cast<std::uint8_t>(value >> 8);
}

void Write32(std::vector<std::uint8_t>& bytes, std::size_t at, std::uint32_t value) {
    for (int i = 0; i < 4; ++i) {
        bytes[at + i] = static_cast<std::uint8_t>(value >> (8 * i));
    }
}

std::uint8_t ExpandMaskedChannel(std::uint32_t packed, std::uint32_t mask) {
    if (mask == 0) return 0;
    unsigned shift = 0;
    while ((mask & 1u) == 0) {
        mask >>= 1;
        ++shift;
    }
    const std::uint64_t value = (packed >> shift) & mask;
    return static_cast<std::uint8_t>((value * 255 + mask / 2) / mask);
}

double Median(const std::array<std::uint64_t, 256>& histogram, std::uint64_t count) {
    const std::uint64_t first = (count - 1) / 2;
    const std::uint64_t second = count / 2;
    std::uint64_t cumulative = 0;
    int firstValue = -1;
    for (int value = 0; value < 256; ++value) {
        cumulative += histogram[value];
        if (firstValue < 0 && cumulative > first) firstValue = value;
        if (cumulative > second) return (firstValue + value) / 2.0;
    }
    throw std::runtime_error("Пустая или повреждённая гистограмма");
}

std::uint8_t CorrectChannel(std::uint8_t value, double gain) {
    return static_cast<std::uint8_t>(std::clamp(std::lround(value * gain), 0L, 255L));
}

} // namespace

Pixel::Pixel(std::uint8_t red, std::uint8_t green, std::uint8_t blue)
    : R(red), G(green), B(blue), Y(0.2126 * red + 0.7152 * green + 0.0722 * blue) {}

Bitmap Bitmap::Load(const std::string& path) {
    std::ifstream file(path, std::ios::binary | std::ios::ate);
    if (!file) throw std::runtime_error("Не удалось открыть файл: " + path);
    const auto length = file.tellg();
    if (length < 54 || static_cast<std::uint64_t>(length) >
                           static_cast<std::uint64_t>(std::numeric_limits<std::streamsize>::max())) {
        throw std::runtime_error("Файл слишком мал или слишком велик для BMP");
    }
    std::vector<std::uint8_t> bytes(static_cast<std::size_t>(length));
    file.seekg(0);
    if (!file.read(reinterpret_cast<char*>(bytes.data()), static_cast<std::streamsize>(bytes.size()))) {
        throw std::runtime_error("Не удалось прочитать BMP полностью");
    }
    if (bytes[0] != 'B' || bytes[1] != 'M') {
        throw std::runtime_error("Файл не имеет сигнатуры BM");
    }

    Bitmap result;
    auto& h = result.header_;
    h.fileSize = Read32(bytes, 2);
    h.reserved = Read32(bytes, 6);
    h.pixelOffset = Read32(bytes, 10);
    h.dibSize = Read32(bytes, 14);
    if (h.dibSize < 40 || std::uint64_t(14) + h.dibSize > bytes.size()) {
        throw std::runtime_error("Поддерживаются заголовки Windows DIB размером от 40 байт");
    }
    h.width = static_cast<std::int32_t>(Read32(bytes, 18));
    h.height = static_cast<std::int32_t>(Read32(bytes, 22));
    h.planes = Read16(bytes, 26);
    h.bitsPerPixel = Read16(bytes, 28);
    h.compression = Read32(bytes, 30);
    h.imageSize = Read32(bytes, 34);
    h.xPixelsPerMeter = static_cast<std::int32_t>(Read32(bytes, 38));
    h.yPixelsPerMeter = static_cast<std::int32_t>(Read32(bytes, 42));
    h.colorsUsed = Read32(bytes, 46);
    h.colorsImportant = Read32(bytes, 50);

    if (h.width <= 0 || h.height == 0 || h.height == std::numeric_limits<std::int32_t>::min() ||
        h.planes != 1 || h.pixelOffset < 14ull + h.dibSize || h.pixelOffset > bytes.size()) {
        throw std::runtime_error("Некорректные размеры, плоскости или смещение пикселей BMP");
    }
    if (h.bitsPerPixel != 1 && h.bitsPerPixel != 4 && h.bitsPerPixel != 8 &&
        h.bitsPerPixel != 16 && h.bitsPerPixel != 24 && h.bitsPerPixel != 32) {
        throw std::runtime_error("Поддерживаются BMP с глубиной 1, 4, 8, 16, 24 и 32 бита");
    }
    if (h.compression != 0 && h.compression != 3) {
        throw std::runtime_error("Поддерживаются только несжатые BMP (BI_RGB и BI_BITFIELDS)");
    }
    if (h.compression == 3 && h.bitsPerPixel != 16 && h.bitsPerPixel != 32) {
        throw std::runtime_error("BI_BITFIELDS поддерживается только для 16/32 бит");
    }

    result.width_ = h.width;
    result.height_ = static_cast<int>(h.height < 0 ? -std::int64_t(h.height) : h.height);
    const auto rowStride = ((std::uint64_t(result.width_) * h.bitsPerPixel + 31) / 32) * 4;
    if (rowStride > (bytes.size() - h.pixelOffset) / std::uint64_t(result.height_)) {
        throw std::runtime_error("Данные пикселей BMP обрезаны");
    }
    const auto count = std::uint64_t(result.width_) * result.height_;
    if (count > result.pixels_.max_size()) {
        throw std::runtime_error("Изображение слишком велико");
    }

    std::vector<Pixel> palette;
    if (h.bitsPerPixel <= 8) {
        const auto paletteSize = h.colorsUsed ? h.colorsUsed : (1u << h.bitsPerPixel);
        if (paletteSize > (1u << h.bitsPerPixel) ||
            std::uint64_t(14) + h.dibSize + std::uint64_t(paletteSize) * 4 > h.pixelOffset) {
            throw std::runtime_error("Повреждена палитра BMP");
        }
        palette.reserve(paletteSize);
        for (std::uint32_t i = 0; i < paletteSize; ++i) {
            const auto at = 14ull + h.dibSize + std::uint64_t(i) * 4;
            palette.emplace_back(bytes[at + 2], bytes[at + 1], bytes[at]);
        }
    }

    std::uint32_t redMask = 0, greenMask = 0, blueMask = 0;
    if (h.compression == 3) {
        const std::uint64_t maskAt = 14ull + 40;
        const std::uint64_t maskEnd = h.dibSize >= 52 ? 14ull + h.dibSize : h.pixelOffset;
        if (maskAt + 12 > maskEnd) throw std::runtime_error("Отсутствуют маски BI_BITFIELDS");
        redMask = Read32(bytes, maskAt);
        greenMask = Read32(bytes, maskAt + 4);
        blueMask = Read32(bytes, maskAt + 8);
        if (!redMask || !greenMask || !blueMask ||
            (redMask & greenMask) || (redMask & blueMask) || (greenMask & blueMask)) {
            throw std::runtime_error("Некорректные маски цветов BMP");
        }
    } else if (h.bitsPerPixel == 16) {
        redMask = 0x7c00;
        greenMask = 0x03e0;
        blueMask = 0x001f;
    }

    result.pixels_.resize(static_cast<std::size_t>(count));
    for (int y = 0; y < result.height_; ++y) {
        const auto fileY = h.height > 0 ? result.height_ - 1 - y : y;
        const auto row = std::uint64_t(h.pixelOffset) + std::uint64_t(fileY) * rowStride;
        for (int x = 0; x < result.width_; ++x) {
            Pixel pixel;
            if (h.bitsPerPixel <= 8) {
                const auto packed = bytes[row + (std::uint64_t(x) * h.bitsPerPixel) / 8];
                const auto shift = 8 - h.bitsPerPixel - (x * h.bitsPerPixel) % 8;
                const auto index = (packed >> shift) & ((1u << h.bitsPerPixel) - 1);
                if (index >= palette.size()) throw std::runtime_error("Индекс палитры вне диапазона");
                pixel = palette[index];
            } else if (h.bitsPerPixel == 24) {
                const auto at = row + std::uint64_t(x) * 3;
                pixel = Pixel(bytes[at + 2], bytes[at + 1], bytes[at]);
            } else if (h.bitsPerPixel == 32 && h.compression == 0) {
                const auto at = row + std::uint64_t(x) * 4;
                pixel = Pixel(bytes[at + 2], bytes[at + 1], bytes[at]);
            } else {
                const auto at = row + std::uint64_t(x) * (h.bitsPerPixel / 8);
                const auto packed = h.bitsPerPixel == 16 ? Read16(bytes, at) : Read32(bytes, at);
                pixel = Pixel(ExpandMaskedChannel(packed, redMask),
                              ExpandMaskedChannel(packed, greenMask),
                              ExpandMaskedChannel(packed, blueMask));
            }
            result.pixels_[std::size_t(y) * result.width_ + x] = pixel;
        }
    }
    return result;
}

Pixel Bitmap::GetPixel(int x, int y) const {
    if (x < 0 || y < 0 || x >= width_ || y >= height_) {
        throw std::out_of_range("Координаты пикселя за пределами изображения");
    }
    return pixels_[std::size_t(y) * width_ + x];
}

int Bitmap::Width() const { return width_; }
int Bitmap::Height() const { return height_; }
const BmpHeader& Bitmap::Header() const { return header_; }

ImageStatistics Bitmap::CalculateStatistics() const {
    ImageStatistics stats;
    double ySum = 0, rSum = 0, gSum = 0, bSum = 0;
    for (const auto& p : pixels_) {
        ++stats.Y.histogram[std::clamp(std::lround(p.Y), 0L, 255L)];
        ++stats.R.histogram[p.R];
        ++stats.G.histogram[p.G];
        ++stats.B.histogram[p.B];
        ySum += p.Y;
        rSum += p.R;
        gSum += p.G;
        bSum += p.B;
    }
    const auto n = static_cast<std::uint64_t>(pixels_.size());
    stats.Y.mean = ySum / n;
    stats.R.mean = rSum / n;
    stats.G.mean = gSum / n;
    stats.B.mean = bSum / n;
    stats.Y.median = Median(stats.Y.histogram, n);
    stats.R.median = Median(stats.R.histogram, n);
    stats.G.median = Median(stats.G.histogram, n);
    stats.B.median = Median(stats.B.histogram, n);
    return stats;
}

WhiteBalanceGains Bitmap::EvaluateWhiteBalance() const {
    double red = 0, green = 0, blue = 0;
    for (const auto& p : pixels_) {
        red += p.R;
        green += p.G;
        blue += p.B;
    }
    const double target = std::max({red, green, blue});
    // Если канал полностью чёрный, усиление не может восстановить его данные.
    return {red > 0 ? target / red : 1.0,
            green > 0 ? target / green : 1.0,
            blue > 0 ? target / blue : 1.0};
}

Bitmap Bitmap::ApplyWhiteBalance() const {
    Bitmap corrected = *this;
    const auto gains = EvaluateWhiteBalance();
    for (auto& p : corrected.pixels_) {
        p = Pixel(CorrectChannel(p.R, gains.R), CorrectChannel(p.G, gains.G),
                  CorrectChannel(p.B, gains.B));
    }
    return corrected;
}

void Bitmap::SaveAs24BitBmp(const std::string& path) const {
    const auto stride = ((std::uint64_t(width_) * 3 + 3) / 4) * 4;
    const auto imageSize = stride * height_;
    if (imageSize > std::numeric_limits<std::uint32_t>::max() - 54) {
        throw std::runtime_error("Изображение слишком велико для 24-битного BMP");
    }
    std::vector<std::uint8_t> bytes(static_cast<std::size_t>(54 + imageSize), 0);
    bytes[0] = 'B'; bytes[1] = 'M';
    Write32(bytes, 2, static_cast<std::uint32_t>(bytes.size()));
    Write32(bytes, 10, 54);
    Write32(bytes, 14, 40);
    Write32(bytes, 18, static_cast<std::uint32_t>(width_));
    Write32(bytes, 22, static_cast<std::uint32_t>(height_));
    Write16(bytes, 26, 1);
    Write16(bytes, 28, 24);
    Write32(bytes, 34, static_cast<std::uint32_t>(imageSize));
    Write32(bytes, 38, static_cast<std::uint32_t>(header_.xPixelsPerMeter));
    Write32(bytes, 42, static_cast<std::uint32_t>(header_.yPixelsPerMeter));
    for (int y = 0; y < height_; ++y) {
        const auto row = 54 + std::uint64_t(height_ - 1 - y) * stride;
        for (int x = 0; x < width_; ++x) {
            const auto& p = pixels_[std::size_t(y) * width_ + x];
            const auto at = row + std::uint64_t(x) * 3;
            bytes[at] = p.B;
            bytes[at + 1] = p.G;
            bytes[at + 2] = p.R;
        }
    }
    std::ofstream out(path, std::ios::binary);
    if (!out || !out.write(reinterpret_cast<const char*>(bytes.data()),
                           static_cast<std::streamsize>(bytes.size()))) {
        throw std::runtime_error("Не удалось записать BMP: " + path);
    }
}
