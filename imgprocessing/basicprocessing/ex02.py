import numpy as np
import matplotlib.pyplot as plt
import collections

SHADES_COUNT = 256


def rgb2mono(img):
    """Converts whole rgb bitmap into mono"""
    return np.array([np.array([pix2mono(pix) for pix in col]) for col in img])


def pix2mono(pix):
    """Counts gray shade for a single pixel"""
    pix = int(0.299 * pix[0] + 0.587 * pix[1] + 0.114 * pix[2])
    if pix not in range(SHADES_COUNT):
        pix = 0
    return pix


def make_histogram(mono_img):
    hist = {}
    for col in mono_img:
        for pix in col:
            if pix not in hist.keys():
                hist[pix] = 1
            else:
                hist[pix] += 1
    return hist


def cumulative_distribution(histogram):
    od = collections.OrderedDict(sorted(histogram.items()))
    count = 0
    cd = {}
    for k, v in od.items():
        count += v
        cd[k] = count
    return cd


def show_histogram(histogram):
    plt.bar(histogram.keys(), histogram.values())
    plt.show()


