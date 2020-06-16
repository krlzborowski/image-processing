# --input --output --fractal --mono --

from projectone import transformations as tr
import cv2
import sys
import collections


def run(args):

    print('Choose transformation:')
    if args.type == 'rgb':
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

    elif args.type == 'bin':
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

    elif args.type == 'mono':
        img = cv2.imread(args.input, 0)
        print('\t(1) Fractal generation\n'
              '\t(2) Kirsch filtration\n'
              '\t(3) Opening with line element')
        option = int(input('Option:\t'))
        if option == 1:
            print('It may take a while...')
            out = tr.generate_fractal(img)
            name = args.input.split('.')[0]
            cv2.imwrite(name + '_fractal_mono.bmp', out)

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