import pygame as pg
imagebackground = pg.image.load('data/background/background.jpg')
scale = True

y = 0
a = 0
def background(win, w, h):
    global scale
    global imagebackground
    global y
    global a
    y += a
    if y > 3:
        a *= -1
    if y < -3:
        a *= -1
    if scale == True:
        imagebackground = pg.transform.scale(imagebackground, (w, h))
        scale = False
    win.blit(imagebackground, (0, y))
    pass
