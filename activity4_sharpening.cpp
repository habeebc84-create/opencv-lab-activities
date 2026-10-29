#include <opencv2/opencv.hpp>
#include <iostream>
#include <cmath>
using namespace cv;
using namespace std;

int main() {
    Mat img = imread("C:/Users/habee/OpenCV/image1.jpg", IMREAD_GRAYSCALE);
    if (img.empty()) { cout << "Image not found!" << endl; return -1; }
    resize(img, img, Size(256, 256));
    // blurred/low-detail input
    Mat blurred;
    GaussianBlur(img, blurred, Size(9, 9), 2.0);

    // 1. Laplacian
    Mat lap;
    Laplacian(blurred, lap, CV_64F);
    Mat lap_sharp(blurred.size(), CV_8U);
    for (int i = 0; i < blurred.rows; i++)
        for (int j = 0; j < blurred.cols; j++)
            lap_sharp.at<uchar>(i, j) = saturate_cast<uchar>(blurred.at<uchar>(i, j) - lap.at<double>(i, j));

    // 2. Sobel
    Mat sx, sy;
    Sobel(blurred, sx, CV_64F, 1, 0, 3);
    Sobel(blurred, sy, CV_64F, 0, 1, 3);
    Mat mag(blurred.size(), CV_8U);
    for (int i = 0; i < blurred.rows; i++)
        for (int j = 0; j < blurred.cols; j++) {
            double m = sqrt(sx.at<double>(i, j) * sx.at<double>(i, j) + sy.at<double>(i, j) * sy.at<double>(i, j));
            mag.at<uchar>(i, j) = saturate_cast<uchar>(m);
        }
    Mat sobel_sharp(blurred.size(), CV_8U);
    for (int i = 0; i < blurred.rows; i++)
        for (int j = 0; j < blurred.cols; j++)
            sobel_sharp.at<uchar>(i, j) = saturate_cast<uchar>(blurred.at<uchar>(i, j) + mag.at<uchar>(i, j));

    // 3. High-pass spatial filtering
    Mat kernel = (Mat_<float>(3, 3) << -1, -1, -1, -1, 8, -1, -1, -1, -1);
    Mat hp;
    filter2D(blurred, hp, CV_64F, kernel);
    Mat hp_sharp(blurred.size(), CV_8U);
    for (int i = 0; i < blurred.rows; i++)
        for (int j = 0; j < blurred.cols; j++)
            hp_sharp.at<uchar>(i, j) = saturate_cast<uchar>(blurred.at<uchar>(i, j) + hp.at<double>(i, j));

    // 4. Unsharp masking
    Mat g;
    GaussianBlur(blurred, g, Size(9, 9), 2.0);
    Mat unsharp(blurred.size(), CV_8U);
    for (int i = 0; i < blurred.rows; i++)
        for (int j = 0; j < blurred.cols; j++) {
            double mask = blurred.at<uchar>(i, j) - g.at<uchar>(i, j);
            unsharp.at<uchar>(i, j) = saturate_cast<uchar>(blurred.at<uchar>(i, j) + 1.5 * mask);
        }

    imwrite("C:/Users/habee/OpenCV/act4_blurred_input.jpg", blurred);
    imwrite("C:/Users/habee/OpenCV/act4_laplacian.jpg", lap_sharp);
    imwrite("C:/Users/habee/OpenCV/act4_sobel.jpg", sobel_sharp);
    imwrite("C:/Users/habee/OpenCV/act4_highpass.jpg", hp_sharp);
    imwrite("C:/Users/habee/OpenCV/act4_unsharp.jpg", unsharp);
    cout << "Activity 4 done." << endl;
    return 0;
}
