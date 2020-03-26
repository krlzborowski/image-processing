
import numpy as np


# a)
def print_size(img):
    width, height = img.shape[:2]
    print("Width: " + str(width) + " Height: " + str(height))


# b)
def compress_image(img):
    compressed_img = np.array([np.array([col for col in row[::2]]) for row in img[::2]])
    return compressed_img


# c)
def brighten_image(img):
    brightness = int(input("Set brightness value (0-255): "))
    if brightness < 0 or brightness > 255:
        raise ValueError
    brighter_img = np.array(
        [np.array([np.array([el + brightness for el in pixel]) for pixel in row]) for row in img])
    return brighter_img


