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
    cum_dist = ex02.cumulative_distribution(histogram)
    x, y = zip(*cum_dist.items())
    plt.plot(x, y)
    plt.show()
    output_shades_count = input("Enter number of output shades: ")


    # cv2.imwrite("basicprocessing/mono_polar.bmp", mono_image)


