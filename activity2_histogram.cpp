
#include <iostream>
using namespace cv;
using namespace std;

int main() {
    Mat img = imread("C:/Users/habee/OpenCV/image1.jpg", IMREAD_GRAYSCALE);
    if (img.empty()) { cout << "Image not found!" << endl; return -1; }
    resize(img, img, Size(256, 256));

    // Reference image for matching (equalized + gamma)
    Mat ref;
    equalizeHist(img, ref);
    // make reference different
    for (int i = 0; i < ref.rows; i++)
        for (int j = 0; j < ref.cols; j++)
            ref.at<uchar>(i, j) = saturate_cast<uchar>(pow(ref.at<uchar>(i, j) / 255.0, 0.8) * 255);

    // Histogram equalization
    Mat eq;
    equalizeHist(img, eq);

    // Histogram matching via CDF
    auto computeCDF = [](const Mat &m) {
        vector<int> hist(256, 0);
        for (int i = 0; i < m.rows; i++)
            for (int j = 0; j < m.cols; j++) hist[m.at<uchar>(i, j)]++;
        vector<double> cdf(256, 0);
        double total = (double)m.rows * m.cols;
        double acc = 0;
        for (int k = 0; k < 256; k++) { acc += hist[k]; cdf[k] = acc / total; }
        return cdf;
    };
    vector<double> srcCDF = computeCDF(img);
    vector<double> refCDF = computeCDF(ref);
    // mapping
    vector<uchar> mapping(256);
    for (int i = 0; i < 256; i++) {
        int j = 0;
        while (j < 255 && refCDF[j] < srcCDF[i]) j++;
        mapping[i] = (uchar)j;
    }
    Mat matched(img.size(), CV_8U);
    for (int i = 0; i < img.rows; i++)
        for (int j = 0; j < img.cols; j++)
            matched.at<uchar>(i, j) = mapping[img.at<uchar>(i, j)];

    imwrite("C:/Users/habee/OpenCV/act2_equalized.jpg", eq);
    imwrite("C:/Users/habee/OpenCV/act2_matched.jpg", matched);
    imwrite("C:/Users/habee/OpenCV/act2_reference.jpg", ref);
    cout << "Activity 2 done." << endl;
    return 0;
}
