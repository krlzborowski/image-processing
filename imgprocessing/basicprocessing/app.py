from imgprocessing.basicprocessing import ex01, ex02
import cv2
import matplotlib.pyplot as plt


def run():
    image = cv2.imread('basicprocessing/polar.bmp')

    # ex01
    ex01.print_size(image)
    # image = ex01.compress_image(image)

    # ex02
    mono_image = ex02.rgb2mono(image)
    histogram = ex02.make_histogram(mono_image)
    ex02.show_histogram(histogram)
    # cum_dist = ex02.cumulative_distribution(histogram)
    # plt.plot('xlabel', 'ylabel', data=cum_dist)
    plt.show()

    # cv2.imwrite("basicprocessing/mono_polar.bmp", mono_image)


