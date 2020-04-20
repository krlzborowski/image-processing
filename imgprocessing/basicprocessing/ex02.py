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
    hist = collections.OrderedDict()
    for i in range(SHADES_COUNT):
        hist[i] = 0
    for col in mono_img:
        for pix in col:
            hist[pix] += 1
    return hist


def cumulative_distribution(histogram):
    count = 0
    cd = {}
    for k, v in histogram.items():
        count += v
        cd[k] = count
    return cd


def show_histogram(histogram):
    plt.bar(histogram.keys(), histogram.values())
    plt.show()


def reduce_colors(img, cum_distr, size, out_shades_count=10):
    """Makes and applies look up table"""
    width, height = size
    n = 0
    lut = []
    for i in range(len(cum_distr)):
        curr_val = list(cum_distr.values())[i]
        if curr_val >= (n + 1) * width * height / out_shades_count:
            n += 1
            if n >= out_shades_count:
                n = out_shades_count - 1
        lut.append(int((SHADES_COUNT - 1) * n / (out_shades_count - 1)))

    return np.array([np.array([lut[pix] for pix in col]) for col in img])
