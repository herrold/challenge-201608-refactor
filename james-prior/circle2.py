#!/usr/bin/env python3

from sys import argv
from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 640, 480


def color(xx, yy):
    z = xx + yy
    c = int(z)
    if c % 2 == 0:
        return '#ffffff'
    else:
        return '#000000'


def main(argv):
    corna = int(argv[1])
    cornb = int(argv[2])
    side = float(argv[3])

    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    x_squareds = [x*x for x in [
        corna + (side * (i/100.0))
        for i in range(WIDTH)]]

    y_squareds = [y*y for y in [
        cornb + (side * (j/100.0))
        for j in range(HEIGHT)]]

    lines = []
    for yy in y_squareds:
        horizontal_line = '{' + ' '.join(
            color(xx, yy)
            for xx in x_squareds) + '}'
        lines.append(horizontal_line)
    img.put(' '.join(lines))

    mainloop()


if __name__ == '__main__':
    main(argv)
