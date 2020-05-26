import numpy as np
import cv2
import math

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
    """
    Performs opening on image using given structural elelment.
    :param np.ndarray img: image to bo processed
    :param np.array strel: structural element
    :return: np.ndarray: processed image
    """
    return dilate(erode(img, strel), strel)


def is_on_boundary(x, y, img, strel):
    """
    Checks if pixel with coordinates x and y is on boundary of image.
    Doesn't include pixels closer than half of the mask.
    :param x: x coordinate
    :param y: y coordinate
    :param img: image to check
    :param strel: structuring element used in morphological function
    :return: boolean
    """
    height, width = img.shape[:2]
    mask_width = strel.shape[0]
    half = int((mask_width - 1) / 2)
    if x <= half or y <= half or x >= width - half or y >= height - half:
        return True
    return False


def erode(img, strel):
    """
    Erodes image with given structuring element.
    :param np.ndarray img: image to erode
    :param np.array strel: structuring element used in erosion
    :return: np.ndarray image after erosion
    """
    height, width = img.shape[:2]
    strel_width = strel.shape[0]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, strel):
                val = img[y][x]
            else:
                center = int((strel_width - 1) / 2)
                neighbours = [img[y + j - center][x + i - center] for j in range(strel_width) for i in
                              range(strel_width)
                              if strel[j][i] == 1]
                val = max(neighbours)
            result[y][x] = val

    return result


def dilate(img, strel):
    """
    Dilates image with given structuring element.
    :param np.ndarray img: np.ndarray img: image to dilate
    :param np.array strel: structuring element used in erosion
    :return: np.ndarray image after erosion
    """
    height, width = img.shape[:2]
    strel_width = strel.shape[0]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, strel):
                val = img[y][x]
            else:
                center = int((strel_width - 1) / 2)
                neighbours = [img[y + j - center][x + i - center] for j in range(strel_width) for i in
                              range(strel_width)
                              if strel[j][i] == 1]
                val = min(neighbours)
            result[y][x] = val

    return result


def create_strel(length, tilt=0):
    """
    Creates structuring element of given length and tilted with given angle for morphological function
    :param int length: length of structuring element
    :param int tilt: angle of tilt
    :return: np.array: created structuring element
    """
    alpha = math.radians(tilt)
    dx = abs(math.cos(alpha))
    dy = abs(math.sin(alpha))

    lgx = length * dx
    n2x = round((lgx - 1) / 2)
    nx = 2 * n2x + 1

    lgy = length * dy
    n2y = round((lgy - 1) / 2)
    ny = 2 * n2y + 1

    result_se = np.zeros([ny, nx])
    if math.cos(alpha) >= 0:
        points = bresenham(0, ny - 1, nx - 1, 0)
    else:
        points = bresenham(nx - 1, ny - 1, 0, 0)

    for x in points:
        result_se[x[1], x[0]] = 1

    return result_se


def bresenham(x1, y1, x2, y2):
    """
    Performs bresenham algorithm of creating line of pixels between two points
    :param int x1: The first point x coordinate
    :param int y1: The first point y coordinate
    :param int x2: The second point x coordinate
    :param int y2: The second point y coordinate
    :return: points: indexes of line points
    :rtype: np.array
    """
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)

    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    dx = x2 - x1
    dy = y2 - y1

    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    if swapped:
        points.reverse()

    return points


# Wypukłe otoczenie

def convex_hull(src_image):
    """
    Computes convex hull on the input image
    :param np.array src_image: The original source image
    :return: result_image: The image after convex hull
    :rtype: np.array
    """
    # create structural elements
    se_0deg = np.array([[1, 1, 0], [1, -1, 0], [1, 0, -1]], dtype=np.int)
    se_45deg = np.array([[1, 1, 1], [1, -1, 0], [0, -1, 0]], dtype=np.int)

    compare = np.zeros_like(src_image)
    result_image = src_image
    # perform hit-or-miss until no change
    while not np.array_equal(result_image, compare):
        compare = result_image

        # hit-or-miss for each se position
        for i in range(4):
            result_image = result_image | hit_miss(result_image, se_0deg)
            result_image = result_image | hit_miss(result_image, se_45deg)
            se_0deg = np.rot90(se_0deg)
            se_45deg = np.rot90(se_45deg)

    return result_image


def hit_miss(src_image, se):
    """
    This method performs hit-or-miss operation
    based on given structuring element
    using logical and of two erosion
    :param np.array src_image: The original source image
    :param np.array se: The structuring element
    :return: result_image: The image after dilation
    :rtype: np.array
    """
    # create mask [0, 1] from [-1, 0, 1]
    true_mask = se * (se == 1)
    false_mask = se * (se == -1) * -1

    # perform two erosion to get hit-or-miss
    result_image = erode(src_image, true_mask) & erode(~src_image, false_mask)

    return result_image
