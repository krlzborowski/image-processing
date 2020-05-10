from imgprocessing.basicprocessing import ex01, ex02, ex03
import cv2
import matplotlib.pyplot as plt
import math


def run():
    image = cv2.imread('basicprocessing/polar.bmp')

    # ex01
    size = ex01.print_size(image)
    # image = ex01.compress_image(image)

    # ex02
    # mono_image = ex02.rgb2mono(image)
    # histogram = ex02.make_histogram(mono_image)
    # print(len(histogram))
    # ex02.show_histogram(histogram)
    # cum_dist = ex02.cumulative_distribution(histogram)
    # x, y = zip(*cum_dist.items())
    # plt.plot(x, y)
    # plt.show()
    # out_shades_count = int(input("Enter number of output shades: "))
    # reduced_image = ex02.reduce_colors(mono_image, cum_dist, size, out_shades_count)
    # cv2.imwrite("basicprocessing/reduced_polar.bmp", reduced_image)

    # ex03
    angle = int(input("Provide angle in degrees to rotate: "))
    angle = math.radians(angle)
    rotated = ex03.rotate(image, angle)
    cv2.imwrite("basicprocessing/rotated.bmp", rotated)



