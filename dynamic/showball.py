import pygame
import values as val
image = [pygame.image.load('data/penguin/snowball_usuall.png')]
def loadimage(scale):
    global image    
    print("s")
    image[0] = pygame.transform.scale(image[0], (image[0].get_width() * scale, image[0].get_height() * scale))

pygame.init()

hit = [pygame.mixer.Sound('data/sound/pen/showball1.wav')]

class showballc():
    destroy = False
    def __init__(self, posx, posy, orient):
        val.showinpen -= 1
        self.posx = posx + 70
        self.posy = posy
        self.count = 30
        self.neg = 1
        self.orient = False
        if orient == "right":
            self.orient = True#right
        else:
            self.posx = posx
        self.down = False
        self.pos = 1
        if self.orient == False:
            self.pos = -1
        

    def blitting(self, win):
        win.blit(image[0], (self.posx, self.posy))
        self.fire()
    def fire(self):
        
        if self.down == False:
            self.posx += self.count * self.pos
            self.count -= 1
            self.posy -= self.count / 20 * self.neg
            if self.count < 20:
                self.neg = self.neg - 2
                self.count += 0.5
            if self.count == 3:
                self.down = True
                self.count = 5
            
        elif self.down:
            self.posx += self.count * self.pos / 2
            
            self.posy -= self.count / 20 * self.neg
            self.count += 0.3
            
        elif self.posx > 10000:
            self.destroy = True
    def collision(self, obj, vidc):
        if self.posy > obj.posy and self.posx > obj.posx and self.posx < obj.posx + obj.width and obj.back == False: 
            if vidc == "platform":
                hit[0].play()
                self.destroy = True
            elif vidc == "hunt" and obj.life > 0:
                obj.life -= 1
                obj.damage = True
                self.destroy = True

        





        


