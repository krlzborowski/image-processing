import cv2
import numpy as np

# ex1

# a)
image = cv2.imread('polar.bmp')
width, height = image.shape[:2]
print("Width: " + str(width) + " Height: " + str(height))

# b)
new_image = image
new_image = np.array([np.array([col for col in row[::2]]) for row in new_image[::2]])
cv2.imwrite('new_polar.bmp', new_image)

# c)
brightness = int(input("Set brightness value (0-255): "))
if brightness < 0 or brightness > 255:
    raise ValueError
brighter_img = np.array([np.array([np.array([el + brightness for el in pixel]) for pixel in row]) for row in new_image])
cv2.imwrite('bright_polar.bmp', brighter_img)


