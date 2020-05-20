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
    cv2.imshow('elo',binary_img)

    mask = tr.create_mask(3)
    dilated = tr.dilate(binary_img, mask)

    collections.Counter(binary_img)
    collections.Counter(dilated)
    # cv2.imshow('dilated', dilated)
    # cv2.imshow('elo',binary_img)
    # cv2.waitKey()