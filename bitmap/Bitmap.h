#pragma once

#include <array>
#include <cstdint>
#include <string>
#include <vector>

struct Pixel {
    std::uint8_t R = 0;
    std::uint8_t G = 0;
    std::uint8_t B = 0;
    double Y = 0.0;

    Pixel() = default;
    Pixel(std::uint8_t red, std::uint8_t green, std::uint8_t blue);
};

struct BmpHeader {
    std::uint32_t fileSize = 0;
    std::uint32_t reserved = 0;
    std::uint32_t pixelOffset = 0;
    std::uint32_t dibSize = 0;
    std::int32_t width = 0;
    std::int32_t height = 0;
    std::uint16_t planes = 0;
    std::uint16_t bitsPerPixel = 0;
    std::uint32_t compression = 0;
    std::uint32_t imageSize = 0;
    std::int32_t xPixelsPerMeter = 0;
    std::int32_t yPixelsPerMeter = 0;
    std::uint32_t colorsUsed = 0;
    std::uint32_t colorsImportant = 0;
};

struct ChannelStatistics {
    std::array<std::uint64_t, 256> histogram{};
    double mean = 0.0;
    double median = 0.0;
};

struct ImageStatistics {
    ChannelStatistics Y;
    ChannelStatistics R;
    ChannelStatistics G;
    ChannelStatistics B;
};

struct WhiteBalanceGains {
    double R = 1.0;
    double G = 1.0;
    double B = 1.0;
};

class Bitmap {
public:
    static Bitmap Load(const std::string& path);

    Pixel GetPixel(int x, int y) const;
    int Width() const;
    int Height() const;
    const BmpHeader& Header() const;

    ImageStatistics CalculateStatistics() const;
    WhiteBalanceGains EvaluateWhiteBalance() const;
    Bitmap ApplyWhiteBalance() const;
    void SaveAs24BitBmp(const std::string& path) const;

private:
    BmpHeader header_;
    int width_ = 0;
    int height_ = 0;
    std::vector<Pixel> pixels_; // Строки идут сверху вниз, как на экране.
};
