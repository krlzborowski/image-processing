# --input --output --fractal --mono --

from projectone import transformations as tr
import cv2
import sys
import collections


def run(args):
    types = args.rgb, args.bin, args.mono
    if sum(types) != 1:
        print('Choose one type of input file: --rgb or --mono or --bin')
        sys.exit(1)

    img = cv2.imread(args.input)
    index = types.index(True)

    print('Choose transformation:\n')
    if index == 0:
        print('\t(1) Kirsch filtration\n')
        option = input()
        if option == '1':
            print('It may take a while...')
            red, green, blue = tr.kirsch_filtration_rgb(img)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_kirsch_red.bmp', red)
            cv2.imwrite(name + '_kirsch_green.bmp', green)
            cv2.imwrite(name + '_kirsch_blue.bmp', blue)
        else:
            print('Wrong option')

    elif index == 1:
        print('\t(1) Opening with line element\n'
              '\t(2) Convex hull\n')
    elif index == 2:
        print('\t(1) Fractal generation\n'
              '\t(2) Kirsch filtration\n'
              '\t(3) Opening with line element')

    # # fractal = tr.generate_fractal(img)
    # # cv2.imshow('Fractal', fractal)
    # # cv2.waitKey()
    # ret, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # # cv2.imshow('elo', binary_img)
    # # cv2.waitKey()
    #
    # # strel = tr.create_strel(10, 45)
    # # opened = tr.line_opening(img, strel)
    # # convex_img = tr.convex_hull(binary_img)
    # # kirsch_img = tr.kirsch_filtration(binary_img)
    # red, green, blue = tr.kirsch_filtration_rgb(img)
    # cv2.imshow('red', red)
    # cv2.imshow('green', green)
    # cv2.imshow('blue', blue)
    # cv2.waitKey()
