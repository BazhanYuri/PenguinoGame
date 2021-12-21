import pygame
import random
from pygame import image
import datetime
import bullet_hunt as bul
import bullet_phy as bulp
import logicgame as log 
pygame.init()

imagehunter = []
isimp = True
def impimag(w, h):
    global imagehunter

    imagehunter = [pygame.image.load('data/hunter/hunter.png'), pygame.image.load('data/hunter/death.png')
    , pygame.image.load('data/hunter/_0000_h.png') , pygame.image.load('data/hunter/_0001_h.png')
    , pygame.image.load('data/hunter/_0002_h.png') , pygame.image.load('data/hunter/_0003_h.png')]

    for i in range(0, len(imagehunter)):
        imagehunter[i] = pygame.transform.scale(imagehunter[i], (int(imagehunter[i].get_width() * w * 1.1), int(imagehunter[i].get_height() * h * 1.1) ))

class hunter:
    
    
    def __init__(self, w, h, posx,posy, radius, life, index):
        self.life = life
        self.procx = w / 100
        self.procy = h / 100
        self.posx = self.procx * posx
        self.posstartx = self.posx 
        self.posy = self.procy * posy
        self.width = 100
        self.back = False
        self.anim = 0
        self.orient = True
        self.neg = 1
        self.radius = radius
        self.coefw = w
        self.sp = False #seeperson
        self.go = True
        self.speed = 1
        self.timefirenow = datetime.datetime.now().second
        self.timefire = datetime.datetime.now().second
        self.anv = "walk"
        self.damage = False
        self.index_pos = index

        self.seefar = 0.2

    def blitt(self, win):
        if self.anv == "walk" and self.anim > 4.8 or self.anim < 2:
            self.anim = 2
        if self.anv == "freez":
            self.anim = 0
        win.blit(pygame.transform.flip(imagehunter[int(self.anim)], self.orient, False), (self.posx,self.posy))
    def freez(self, win):
        self.anv = "freez"
        win.blit(imagehunter[1], (self.posx,self.posy))
    #def checkyou(self, obj):
       
    def seeyou(self, obj):
        if abs(self.posx - obj.posx) < self.coefw * self.seefar:
            self.sp = True
            
            if self.posx < obj.posx :
                self.orient = True
                self.go = True
                self.neg = 1
            else:
                self.orient = False
                self.go = False
                self.neg = -1
            self.fire()
        else:
            self.sp = False
            if self.go == True:
                self.orient = True
            else:
                self.orient = False
    def fire(self):
        #print("time now " , datetime.datetime.now().second, "timefire", self.timefire)
        if datetime.datetime.now().second == 0:
            self.timefire = 2
        
        if datetime.datetime.now().second > self.timefire + 2:
            self.seefar = random.uniform(0.2, 0.5)
            bulp.bullet_list.append(bul.bulet(self.posx, self.posy, "drob", self.orient))
            self.timefire = datetime.datetime.now().second
            
    def damagedef(self):
        if self.damage:
            log.is_hunt[log.level - 1][self.index_pos] -= 1
            self.damage = False        


    def walk(self) :
        self.anv = "walk"
        self.posx += self.speed * self.neg
        self.anim += 0.1
        if self.neg == 1:
            self.orient = True
            self.go = True
        else:
            self.orient = False
            self.go = False
        if self.posstartx + self.radius < self.posx and self.go == True:
            self.neg *= -1
            self.speed = random.uniform(1.0, 2.0)
            
        if self.posstartx  > self.posx and self.go == False:
            self.neg *= -1
            self.speed = random.uniform(1.0, 2.0)
            
            
def main(win, w, h, list_hunt, obj):
    global isimp
    global imagehunter
    if isimp:
        impimag(w, h)
        isimp = False
    if len(list_hunt) > 0:
        for i in range(0, len(list_hunt)):
           list_hunt[i].blitt(win)
           list_hunt[i].damagedef()
           
           
           if list_hunt[i].life > 0:

                if list_hunt[i].sp == False:
                    list_hunt[i].walk()
                list_hunt[i].seeyou(obj)
           list_hunt[i].width = imagehunter[0].get_width()
           if list_hunt[i].life < 1:
               list_hunt[i].freez(win)
               
               
    
    


