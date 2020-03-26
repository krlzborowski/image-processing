import cv2
import numpy as np
import matplotlib.pyplot as plt
import ex01


def rgb2mono(img):
    mono_img = np.array(
        [np.array(
            [0.299 * pix[0] + 0.587 * pix[1] + 0.114 * pix[2]
                for pix in col])
            for col in img])

    return mono_img


def make_histogram(img):
    hist = {}
    for col in img:
        for pix in col:
            if pix[0] not in hist.keys():
                hist[pix[0]] = 1
            else:
                hist[pix[0]] += 1
    return hist



