# --input --output --fractal --mono --

from projectone import transformations as tr
import cv2


def run():
    img = cv2.imread('mono_polar.bmp', 0)
    fractal = tr.generate_fractal(img)
    cv2.imshow('Fractal', fractal)
    cv2.waitKey()
