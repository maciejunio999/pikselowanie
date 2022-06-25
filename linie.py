# ten program pozwala jedynie zobrazować sobie jak duże będą piksele w zależności od wybranej liczby

from PIL import Image, ImageDraw
import math

#im = Image.open(r"jan.jpg")
#im = Image.open(r"ala.jpg")
im = Image.open(r"ja.jpg")
roz = im.size
ilosc_pikseli = []


def linie(x1, y1, x2, y2, zdj):
    draw = ImageDraw.Draw(zdj)
    # draw.line((początekx, począteky, koniecx, koniecy), fill=kolor, width=szerokość)
    draw.line((x1, y1, x2, y2), fill=128, width=1)


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def funkcja(imm, z1=0, z2=0):
    inpt = int(input("Szerokość piksela: "))
    for i in range(0, len(roz)):
        ilosc_pikseli.append(int(round_down(roz[i] / inpt)))

    while z1 < roz[0]:
        z1 += inpt
        linie(z1, 0, z1, roz[1], imm)

    while z2 < roz[1]:
        z2 += inpt
        linie(0, z2, roz[0], z2, imm)





try:
    funkcja(im)
except ValueError:
    print("Zła wartość!")
    funkcja(im)

im.show()

