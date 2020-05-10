import numpy as np
import math


def rotate(image, angle):
    cos = math.cos(angle)
    sin = math.sin(angle)
    height, width = image.shape[:2]
    center_x = width / 2
    center_y = height / 2
    new_image = np.zeros((height, width, 3), np.int8)

    for x in range(width):
        for y in range(height):
            new_x = round(center_x + (x - center_x) * cos - (y - center_y) * sin)
            new_y = round(center_y + (x - center_x) * sin + (y - center_y) * cos)
            if 0 <= new_x < width and 0 <= new_y < height:
                new_image[new_y][new_x] = image[y][x]

    return new_image
