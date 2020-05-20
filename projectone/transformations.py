import numpy as np
import cv2

affine_tables = [
    [[-0.67, -0.02, 0], [-0.18, 0.81, 10], [0, 0, 1]],
    [[0.4, 0.4, 0], [-0.1, 0.4, 0], [0, 0, 1]],
    [[-0.4, -0.4, 0], [-0.1, 0.4, 0], [0, 0, 1]],
    [[-0.1, 0, 0], [0.44, 0.44, -2], [0, 0, 1]]
]


# Generowanie fraktali metodą z rozdz. 2.7 (punktowe) mono

def generate_fractal(img):
    # TODO: choose random table
    # TODO: affine transformation for every pixel generated coordinate value increased by 1
    fractal = np.copy(img)
    table = affine_tables[1]
    height, width = img.shape[:2]
    for x in range(width):
        for y in range(height):
            x_new = int((table[0][0] * x + table[1][0] * y + table[2][0]) / \
                        (table[0][2] * x + table[1][2] * y + table[2][2]))
            y_new = int((table[0][1] * x + table[1][1] * y + table[2][1]) / \
                        (table[0][2] * x + table[1][2] * y + table[2][2]))
            fractal[x_new][y_new] += 1
    return fractal


# Filtracja Kirscha, Brzeg - odbicie symetryczne. Dla RGB każda warstwa osobno

# Otwarcie elementem linijnym o zadanej długosći i nachyleniu


def line_opening(img, strel):
    return dilate(erode(img, strel), strel)


def is_on_boundary(x, y, img, mask):
    height, width = img.shape[:2]
    mask_width = mask.shape[0]
    half = int(mask_width/2)
    if x <= half or y == 0 or x >= width - half or y == height:
        return True
    return False


def erode(img, strel):
    height, width = img.shape[:2]
    strel_width = strel.shape[0]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, strel):
                val = img[y][x]
            else:
                center = int(strel_width / 2)
                neighbours = [img[y + j - center][x + i - center] for j in range(strel_width) for i in range(strel_width)
                              if strel[j][i] == 1]
                val = max(neighbours)
            result[y][x] = val

    return result


def dilate(img, strel):
    height, width = img.shape[:2]
    strel_width = strel.shape[0]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, strel):
                val = img[y][x]
            else:
                center = int(strel_width / 2)
                neighbours = [img[y + j - center][x + i - center] for j in range(strel_width) for i in range(strel_width)
                              if strel[j][i] == 1]
                val = min(neighbours)
            result[y][x] = val

    return result


def create_strel(length, tilt=0):
    # TODO specify tilt of the strel

    if tilt == 0:
        strel = np.zeros((length, length), dtype=int)
        strel[int(length / 2)] = np.ones(length, dtype=int)
        return strel
    else:
        strel = np.zeros((length, length), dtype=int)


# Wypukłe otoczenie

def convex_hull():
    pass
