import math
from PIL import Image

im = Image.open(r"jaa.jpg")


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def round_half_away_from_zero(n, decimals=0):
    rounded_abs = round_half_up(abs(n), decimals)
    return math.copysign(rounded_abs, n)


# rgb = ImageGrab.grab().load()[1, 1]

width, height = im.size


def sr_rgb_pikseli(bok, startx, starty, zdj):
    pixels = zdj.load()
    rgb = [0, 0, 0]
    try:
        for y in range(starty, starty + bok-1):  # iteracja po rzedach
            for x in range(startx, startx + bok-1):  # iteracja po kolumnach
                r, g, b = pixels[x, y]
                rgb[0] = rgb[0] + r
                rgb[1] = rgb[1] + g
                rgb[2] = rgb[2] + b
    except IndexError:
        print(str(y)+"koniec"+str(x))

    for i in range(len(rgb)):
        rgb[i] = int(round_half_away_from_zero(rgb[i] / (bok * bok)))
    try:
        for m in range(starty, starty + bok):  # iteracja po rzędach
            for n in range(startx, startx + bok):  # iteracja po kolumnach
                zdj.putpixel((n, m), tuple(rgb))
    except IndexError:
        print(str(m)+"koniec"+str(n))

    #zdj.show()


piksel = 40
iloscpikseli = []
w, h = im.size
iloscpikseli.append(int(round_down(w / piksel)))
iloscpikseli.append(int(round_down(h / piksel)))

imz = im.crop((0, 0, piksel * iloscpikseli[0], piksel * iloscpikseli[1]))
wz, hz = imz.size

rozz = imz.size

print(wz, hz)

for i in range(0, hz, piksel):
    for j in range(0, wz, piksel):
        sr_rgb_pikseli(piksel, j, i, imz)

imz.show()

