import pygame as py
import values as val
image = [py.image.load('data/hunter/bullet.png')]

isscale = True
def imagescale(w, h):
    global image
    for i in range(0, len(image)):
        image[i] = py.transform.scale(image[i], (int(w * 0.01), int(h * 0.01)))

class bulet:
    global image
    def __init__(self, x, y, vid, orient):
        self.x = x
        
        self.image = image[0]
        self.speed = 1
        if orient == True:
            self.neg = 1
        else:
            self.neg = -1
        if vid == "drob":
            self.image = image[0]
            self.speed = 5
            self.y = y * 1.07
            if orient == True:
                self.x = x * 1.08
            else:
                self.x = x * 1

    
    def blitt(self, win):
        win.blit(self.image, (self.x, self.y))
        self.x += self.speed * self.neg
    def shot(self, obj):
        if self.x > obj.posx and self.x < obj.posx + obj.width and self.y < obj.posy + obj.height and self.y > obj.posy:
            val.lifepen -= 1
            return True


