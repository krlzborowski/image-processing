import numpy as np
import math
import random


def generate_fractal(img):
    """
    Generate fractal from image using affine transformations
    :param np.ndarray img: input image
    :returnn np.ndarray: generated fractal image
    """
    affine_tables = [
        [[-0.67, -0.02, 0], [-0.18, 0.81, 10], [0, 0, 1]],
        [[0.4, 0.4, 0], [-0.1, 0.4, 0], [0, 0, 1]],
        [[-0.4, -0.4, 0], [-0.1, 0.4, 0], [0, 0, 1]],
        [[-0.1, 0, 0], [0.44, 0.44, -2], [0, 0, 1]]
    ]

    height, width = img.shape[:2]
    fractal = np.zeros((height, width), dtype='uint8')
    x = random.randint(0, width)
    y = random.randint(0, height)
    z = 1
    matrix = np.array([[x], [y], [z]], dtype=np.int)
    fractal[y, x] = 1

    for i in range(10000000):
        table = np.array(affine_tables[random.randint(0, 3)], dtype=np.float)
        matrix = table @ matrix
        x = math.floor(20 * matrix[0, 0] + width / 2)
        y = math.floor(20 * matrix[1, 0] + height / 2)
        if 0 <= x < width and 0 <= y < height:
            if fractal[y, x] < 255:
                fractal[y, x] += 1

    return fractal


def symmetric_boundary(img):
    """
    Extends image with pixels mirrored from the edge neighbourhood
    :param np.ndarray img: image to be extended
    :return: np.ndarray: extended image
    """
    result = np.insert(img, 0, img[1], 0)
    result = np.append(result, result[[-2], :], 0)
    result = np.insert(result, 0, result[:, 1], 1)
    result = np.append(result, result[:, [-2]], 1)
    return result


def kirsch_filtration(img):
    """
    Filter using kirsch operator
    :param np.ndarray img: image to be filtered
    :return: np.ndarray: image after filtration
    """
    kirsch_0deg = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]], dtype=np.int)
    kirsch_45deg = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]], dtype=np.int)

    extended_img = symmetric_boundary(img)
    result = np.ndarray(img.shape, dtype='uint8')
    height, width = img.shape[:2]

    for x in range(width):
        for y in range(height):
            values = []
            for k in range(4):
                kirsch_0deg = np.rot90(kirsch_0deg)
                kirsch_45deg = np.rot90(kirsch_45deg)
                sum0 = 0
                sum45 = 0
                for i in range(3):
                    for j in range(3):
                        sum0 += kirsch_0deg[j][i] * extended_img[y + j][x + i]
                        sum45 += kirsch_45deg[j][i] * extended_img[y + j][x + i]

                values.append(sum0)
                values.append(sum45)

            result[y][x] = max(values)

    return result


def kirsch_filtration_rgb(img):
    """
    Does kirsch filtration for each color layer separately
    :param np.ndarray img: 3d array of rgb image to be filtrated
    :return: np.ndarray: each color layer filtrated in rgb np.ndarray image
    """
    result = np.ndarray(img.shape, dtype='uint8')
    for i in range(3):
        result[..., i] = kirsch_filtration(img[..., i])
    return result


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
    strel_height, strel_width = strel.shape[:2]
    x_center = math.floor(strel_width / 2)
    y_center = math.floor(strel_height / 2)
    if x <= x_center or y <= y_center or x >= width - x_center or y >= height - y_center:
        return True
    return False


def dilate(img, strel):
    """
    Erodes image with given structuring element.
    :param np.ndarray img: image to erode
    :param np.array strel: structuring element used in erosion
    :return: np.ndarray image after erosion
    """
    height, width = img.shape[:2]
    strel_height, strel_width = strel.shape[:2]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, strel):
                val = 0
            else:
                x_center = math.floor(strel_width / 2)
                y_center = math.floor(strel_height / 2)
                neighbours = [img[y + j - y_center][x + i - x_center] for j in range(strel_height) for i in
                              range(strel_width)
                              if strel[j][i] == 1]
                val = max(neighbours)
            result[y][x] = val

    return result


def erode(img, strel):
    """
    Dilates image with given structuring element.
    :param np.ndarray img: np.ndarray img: image to dilate
    :param np.array strel: structuring element used in erosion
    :return: np.ndarray image after erosion
    """
    height, width = img.shape[:2]
    strel_height, strel_width = strel.shape[:2]
    result = np.ndarray(img.shape, dtype='uint8')

    for x in range(width):
        for y in range(height):
            if is_on_boundary(x, y, img, strel):
                val = 0
            else:
                x_center = math.floor(strel_width / 2)
                y_center = math.floor(strel_height / 2)
                neighbours = [img[y + j - y_center][x + i - x_center] for j in range(strel_height) for i in
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


def convex_hull(src_image):
    """
    Computes convex hull on the input image
    :param np.array src_image: The original source image
    :return: result_image: The image after convex hull
    :rtype: np.array
    """
    se_0deg = np.array([[1, 1, 0], [1, -1, 0], [1, 0, -1]], dtype=np.int)
    se_45deg = np.array([[1, 1, 1], [1, -1, 0], [0, -1, 0]], dtype=np.int)

    compare = np.zeros_like(src_image)
    result_image = src_image
    while not np.array_equal(result_image, compare):
        compare = result_image

        for i in range(4):
            result_image = result_image | hit_miss(result_image, se_0deg)
            result_image = result_image | hit_miss(result_image, se_45deg)
            se_0deg = np.rot90(se_0deg)
            se_45deg = np.rot90(se_45deg)

    return result_image


def hit_miss(src_image, se):
    """
    Performs hit-or-miss operation based on given structuring element using logical and of two erosion
    :param np.array src_image: The original source image
    :param np.array se: The structuring element
    :return: result_image: The image after dilation
    :rtype: np.array
    """
    true_mask = se * (se == 1)
    false_mask = se * (se == -1) * -1
    result_image = erode(src_image, true_mask) & erode(~src_image, false_mask)
    return result_image
