#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

int main() {
    Mat img = imread("C:/Users/habee/OpenCV/image1.jpg", IMREAD_GRAYSCALE);
    if (img.empty()) { cout << "Image not found!" << endl; return -1; }
    resize(img, img, Size(256, 256));
    int L = 256;

    // 1. Image negative
    Mat neg = L - 1 - img;

    // 2. Logarithmic transformation
    double maxVal;
    minMaxLoc(img, nullptr, &maxVal);
    double c_log = (L - 1) / log(1 + maxVal);
    Mat log_img(img.size(), CV_8U);
    for (int i = 0; i < img.rows; i++)
        for (int j = 0; j < img.cols; j++)
            log_img.at<uchar>(i, j) = saturate_cast<uchar>(c_log * log(1 + img.at<uchar>(i, j)));

    // 3. Power-law (Gamma) gamma=0.5 and 2.0
    auto gammaTransform = [&](double gamma) {
        Mat out(img.size(), CV_8U);
        double c = (L - 1) / pow((double)(L - 1), gamma);
        for (int i = 0; i < img.rows; i++)
            for (int j = 0; j < img.cols; j++)
                out.at<uchar>(i, j) = saturate_cast<uchar>(c * pow(img.at<uchar>(i, j), gamma));
        return out;
    };
    Mat gamma_05 = gammaTransform(0.5);
    Mat gamma_20 = gammaTransform(2.0);

    // 4. Contrast stretching
    double rmin, rmax;
    minMaxLoc(img, &rmin, &rmax);
    Mat stretch(img.size(), CV_8U);
    if (rmax - rmin == 0) img.copyTo(stretch);
    else for (int i = 0; i < img.rows; i++)
        for (int j = 0; j < img.cols; j++)
            stretch.at<uchar>(i, j) = saturate_cast<uchar>((img.at<uchar>(i, j) - rmin) / (rmax - rmin) * (L - 1));

    imwrite("C:/Users/habee/OpenCV/act1_negative.jpg", neg);
    imwrite("C:/Users/habee/OpenCV/act1_log.jpg", log_img);
    imwrite("C:/Users/habee/OpenCV/act1_gamma_0.5.jpg", gamma_05);
    imwrite("C:/Users/habee/OpenCV/act1_gamma_2.0.jpg", gamma_20);
    imwrite("C:/Users/habee/OpenCV/act1_contrast_stretch.jpg", stretch);

    // Side-by-side
    Mat row1, row2, combined;
    hconcat(img, neg, row1);
    // (simplified: just print done)
    cout << "Activity 1 done." << endl;
    return 0;
}
