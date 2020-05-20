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


def line_opening(img, length, tilt):
    mask = create_mask(length)
    erode(img, mask)
    dilate(img, mask)
    return


def is_on_boundary(x, y, img, mask):
    height, width = img.shape[:2]
    mask_width = mask.shape[0]
    half = int(mask_width/2)
    if x <= half or y == 0 or x >= width - half or y == height:
        return True
    return False


def erode(img, mask):
    pass


def dilate(img, mask):
    height, width = img.shape[:2]
    mask_width = mask.shape[0]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, mask):
                val = img[y][x]
            else:
                center = int(mask_width / 2)
                neighbours = [img[y + j - center][x + i - center] for j in range(mask_width) for i in range(mask_width)
                              if mask[j][i] == 1]
                val = max(neighbours)
            result[y][x] = val

    return result


def create_mask(length, tilt=0):
    # TODO specify tilt of the mask

    if tilt == 0:
        mask = np.zeros((length, length), dtype=int)
        mask[int(length / 2)] = np.ones(length, dtype=int)
        return mask
    else:
        mask = np.zeros((length, length), dtype=int)


# Wypukłe otoczenie

def convex_surroundings():
    pass
