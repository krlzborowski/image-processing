# --input --output --fractal --mono --

from projectone import transformations as tr
import cv2
import collections


def run():
    img = cv2.imread('w_shape.png')
    # fractal = tr.generate_fractal(img)
    # cv2.imshow('Fractal', fractal)
    # cv2.waitKey()
    ret, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # cv2.imshow('elo', binary_img)
    # cv2.waitKey()

    # strel = tr.create_strel(10, 45)
    # opened = tr.line_opening(img, strel)
    # convex_img = tr.convex_hull(binary_img)
    # kirsch_img = tr.kirsch_filtration(binary_img)
    red, green, blue = tr.kirsch_filtration_rgb(img)
    cv2.imshow('red', red)
    cv2.imshow('green', green)
    cv2.imshow('blue', blue)
    cv2.waitKey()
