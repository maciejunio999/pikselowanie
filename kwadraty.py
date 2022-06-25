# początkowy kod uśredniający wartości rgb pojedyńczych pikseli nie działał w przypadku
# iteracji od miejsca innego niż punkt (0,0), ten natomiast już to umożliwia

import math
from PIL import Image

im = Image.open(r"jaa.jpg")


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)


def sr_rgb_pikseli(bok, start, zdj):
    pixels = zdj.load()
    rgb = [0, 0, 0]

    for y in range(start, start + bok):  # iteracja po rzędach
        for x in range(start, start + bok):  # iteracja po kolumnach
            r, g, b = pixels[x, y]
            rgb[0] = rgb[0] + r
            rgb[1] = rgb[1] + g
            rgb[2] = rgb[2] + b

    print(rgb)
    for i in range(len(rgb)):
        rgb[i] = int(round_half_away_from_zero(rgb[i] / (bok * bok)))
    print(rgb)

    for m in range(start, start + bok):  # iteracja po rzędach
        for n in range(start, start + bok):  # iteracja po kolumnach
            zdj.putpixel((m, n), tuple(rgb))

    zdj.show()


#sr_rgb_pikseli(40, 120, im)

w, h = im.size
z = 0
pixels = im.load()
for i in range(1000, w):
    krot = pixels[i, 0]
    print(krot)
    z += 1
print(z)
print(z == w)
