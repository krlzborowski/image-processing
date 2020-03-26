from . basicprocessing import ex01, ex02
import cv2


def run():
    image = cv2.imread('polar.bmp')

    # ex01
    ex01.print_size(image)
    image = ex01.compress_image(image)

    # ex02
    mono_image = ex02.rgb2mono(image)

    # histogram = make_histogram(image)
    # x = list(histogram.keys())
    # y = list(histogram.values())
    # plt.hist(x=histogram, bins="auto")
    # plt.show()
    cv2.imwrite("mono_polar.bmp", mono_image)
    # print(histogram)
