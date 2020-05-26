# --input --output --fractal --mono --

from projectone import transformations as tr
import cv2
import collections


def run():
    img = cv2.imread('mono_polar.bmp', 0)
    # fractal = tr.generate_fractal(img)
    # cv2.imshow('Fractal', fractal)
    # cv2.waitKey()
    ret, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('elo', binary_img)
    # cv2.waitKey()

    strel = tr.create_strel(10, 45)
    # binary = binary_img
    opened = tr.line_opening(binary_img, strel)

    cv2.imshow('intput', binary_img)
    cv2.imshow('open', opened)
    cv2.waitKey()
