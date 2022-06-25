# funkcja robiąca listę zawierajacą średnią wartośc liczb dodanych do indeksów


def funk(l, z):
    for x in range(0, z):
        if x == 0:
            l[0] = (l[0] + (x + 1)) / (x + 2)
            l[1] = (l[1] + (x + 1)) / (x + 2)
        elif x > 0:
            l[0] = (l[0] * x + (x + 1)) / (x + 2)
            l[1] = (l[1] * x + (x + 1)) / (x + 2)
    return l


print(funk([0, 2], 4))
