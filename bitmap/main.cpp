#include "Bitmap.h"

#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {

void PrintHeader(const BmpHeader& h) {
    std::cout << "BMP header\n"
              << "Signature: BM\n"
              << "File size: " << h.fileSize << '\n'
              << "Reserved: " << h.reserved << '\n'
              << "Pixel offset: " << h.pixelOffset << '\n'
              << "DIB size: " << h.dibSize << '\n'
              << "Width: " << h.width << '\n'
              << "Height: " << h.height << '\n'
              << "Planes: " << h.planes << '\n'
              << "Bits per pixel: " << h.bitsPerPixel << '\n'
              << "Compression: " << h.compression << '\n'
              << "Image size: " << h.imageSize << '\n'
              << "X pixels per meter: " << h.xPixelsPerMeter << '\n'
              << "Y pixels per meter: " << h.yPixelsPerMeter << '\n'
              << "Colors used: " << h.colorsUsed << '\n'
              << "Colors important: " << h.colorsImportant << "\n\n";
}

void PrintCorner(const char* name, Pixel p) {
    std::cout << name << ": R: " << int(p.R) << " G: " << int(p.G)
              << " B: " << int(p.B) << '\n';
}

void PrintChannel(const char* name, const ChannelStatistics& channel) {
    std::cout << name << " mean: " << channel.mean
              << ", median: " << channel.median << '\n';
    std::cout << name << " histogram (value: count):";
    for (int value = 0; value < 256; ++value) {
        if (channel.histogram[value] != 0) {
            std::cout << ' ' << value << ':' << channel.histogram[value];
        }
    }
    std::cout << '\n';
}

void PrintStatistics(const ImageStatistics& stats) {
    PrintChannel("Y", stats.Y);
    PrintChannel("R", stats.R);
    PrintChannel("G", stats.G);
    PrintChannel("B", stats.B);
}

} // namespace

int main(int argc, char** argv) {
    if (argc > 3) {
        std::cerr << "Usage: bitmap [input.bmp] [balanced-output.bmp]\n";
        return 1;
    }
    const std::string path = argc > 1 ? argv[1] : "image.bmp";
    try {
        const auto image = Bitmap::Load(path);
        PrintHeader(image.Header());
        std::cout << "Corners (coordinates from top left)\n";
        PrintCorner("Top left", image.GetPixel(0, 0));
        PrintCorner("Top right", image.GetPixel(image.Width() - 1, 0));
        PrintCorner("Bottom left", image.GetPixel(0, image.Height() - 1));
        PrintCorner("Bottom right", image.GetPixel(image.Width() - 1, image.Height() - 1));

        std::cout << std::fixed << std::setprecision(2) << "\nOriginal image\n";
        PrintStatistics(image.CalculateStatistics());
        const auto gains = image.EvaluateWhiteBalance();
        std::cout << "\nWhite balance gains: R=" << gains.R
                  << " G=" << gains.G << " B=" << gains.B << '\n';
        const auto balanced = image.ApplyWhiteBalance();
        std::cout << "\nAfter white balance\n";
        PrintStatistics(balanced.CalculateStatistics());
        if (argc == 3) {
            if (path == argv[2]) throw std::runtime_error("Выходной файл должен отличаться от входного");
            balanced.SaveAs24BitBmp(argv[2]);
            std::cout << "Saved: " << argv[2] << '\n';
        }
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << '\n';
        return 1;
    }
}
