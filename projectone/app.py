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

    index = types.index(True)

    print('Choose transformation:')
    if index == 0:
        img = cv2.imread(args.input)
        print('\t(1) Kirsch filtration\n')
        option = int(input('Option:\t'))
        if option == 1:
            print('It may take a while...')
            red, green, blue = tr.kirsch_filtration_rgb(img)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_kirsch_red.bmp', red)
            cv2.imwrite(name + '_kirsch_green.bmp', green)
            cv2.imwrite(name + '_kirsch_blue.bmp', blue)
        else:
            print('Wrong option - select number of desired transformation and press enter')

    elif index == 1:
        img = cv2.imread(args.input, 0)
        print('\t(1) Opening with line element\n'
              '\t(2) Convex hull\n')
        option = int(input('Option:\t'))
        if option == 1:
            length = int(input('Length of structuring element:\t'))
            degrees = int(input('Rotation for structuring element in degrees:\t'))
            print('It may take a while...')
            strel = tr.create_strel(length, degrees)
            out = tr.line_opening(img, strel)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_opening_bin.bmp', out)
        elif option == 2:
            print('It may take a while...')
            out = tr.convex_hull(img)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_convex_hull.bmp', out)
        else:
            print('Wrong option - select number of desired transformation and press enter')

    elif index == 2:
        img = cv2.imread(args.input, 0)
        print('\t(1) Fractal generation\n'
              '\t(2) Kirsch filtration\n'
              '\t(3) Opening with line element')
        option = int(input('Option:\t'))
        if option == 1:
            print('Not implemented')
        elif option == 2:
            print('It may take a while...')
            out = tr.kirsch_filtration(img)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_kirsch_mono.bmp', out)
        elif option == 3:
            length = int(input('Length of structuring element:\t'))
            degrees = int(input('Rotation for structuring element in degrees:\t'))
            print('It may take a while...')
            strel = tr.create_strel(length, degrees)
            out = tr.line_opening(img, strel)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_opening_mono.bmp', out)
        else:
            print('Wrong option - select number of desired transformation and press enter')

    # img = cv2.imread('dziury.bmp', 0)
    # # fractal = tr.generate_fractal(img)
    # # cv2.imshow('Fractal', fractal)
    # # cv2.waitKey()
    # ret, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # # cv2.imshow('elo', binary_img)
    # # cv2.waitKey()
    #
    # # strel = tr.create_strel(15, 70)
    # # eroded = tr.erode(binary_img, strel)
    # # dilated = tr.dilate(binary_img, strel)
    # # opened = tr.line_opening(img, strel)
    # convex_img = tr.convex_hull(binary_img)
    # # kirsch_img = tr.kirsch_filtration(binary_img)
    # # red, green, blue = tr.kirsch_filtration_rgb(img)
    # # cv2.imshow('eroded', eroded)
    # # cv2.imshow('dilated', dilated)
    # cv2.imshow('convex', convex_img)
    # cv2.imshow('input', img)
    # cv2.waitKey()
