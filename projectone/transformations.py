import numpy as np

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
    pass


def erode():
    pass


def dilate():
    pass

# Wypukłe otoczenie
