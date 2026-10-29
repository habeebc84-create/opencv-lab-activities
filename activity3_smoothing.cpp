#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

int main() {
    Mat img = imread("C:/Users/habee/OpenCV/image1.jpg", IMREAD_GRAYSCALE);
    if (img.empty()) { cout << "Image not found!" << endl; return -1; }
    resize(img, img, Size(256, 256));

    // Add salt-and-pepper noise
    Mat noisy = img.clone();
    double prob = 0.05;
    RNG rng(12345);
    for (int i = 0; i < noisy.rows; i++)
        for (int j = 0; j < noisy.cols; j++) {
            double r = (double)rng / (double)RNG::MAX;
            if (r < prob / 2) noisy.at<uchar>(i, j) = 0;
            else if (r > 1 - prob / 2) noisy.at<uchar>(i, j) = 255;
        }

    Mat mean3, mean5, median3, gauss;
    blur(noisy, mean3, Size(3, 3));
    blur(noisy, mean5, Size(5, 5));
    medianBlur(noisy, median3, 3);
    GaussianBlur(noisy, gauss, Size(5, 5), 1.0);

    imwrite("C:/Users/habee/OpenCV/act3_noisy.jpg", noisy);
    imwrite("C:/Users/habee/OpenCV/act3_mean3.jpg", mean3);
    imwrite("C:/Users/habee/OpenCV/act3_mean5.jpg", mean5);
    imwrite("C:/Users/habee/OpenCV/act3_median3.jpg", median3);
    imwrite("C:/Users/habee/OpenCV/act3_gaussian.jpg", gauss);
    cout << "Activity 3 done." << endl;
    return 0;
}
