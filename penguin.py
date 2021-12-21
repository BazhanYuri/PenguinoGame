import pygame as pg
from pygame import display
import platforms as pl
import values as val
import logicgame as log
from level import part_1
from dynamic import physic as phy
from dynamic import showball as showb
import datetime

gravity = True
time = 0
pg.init()
class penguin():

    sound1 = pg.mixer.Sound('data/sound/pen/walk_show_1.wav')
    anim = "walk"
    animation = 0
    orientation = "right"
    #timefire
    
    global gravity
    def __init__(self, w, h, cw, ch):
        self.image = [pg.image.load('data/penguin/walk_0000_1.png'), pg.image.load('data/penguin/walk_0001_2.png')
        ,pg.image.load('data/penguin/walk_0002_3.png'), pg.image.load('data/penguin/walk_0003_4.png'),
        pg.image.load('data/penguin/jump_0001.png')
        ,pg.image.load('data/penguin/jump_0002.png'), pg.image.load('data/penguin/jump_0003.png')
        ,pg.image.load('data/penguin/fire_0000.png'), pg.image.load('data/penguin/jump_0001.png')
        ,pg.image.load('data/penguin/fire_0002.png'), pg.image.load('data/penguin/jump_0003.png')#10
        ,pg.image.load('data/penguin/make_ball_0000.png'), pg.image.load('data/penguin/make_ball_0001.png')]
        
        
        for i in range(0, len(self.image)):

            self.image[i] = pg.transform.scale(self.image[i], (int(self.image[i].get_width() * cw) , int(self.image[i].get_height() * ch)))
        self.countgrav = 1
        self.oldsecond = datetime.datetime.now().second
        self.rect = self.image[0].get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.isJump = False
        self.jumpCount = 10
        self.posx = 0
        self.posy = h / 1.6
        self.speed = 1
        self.stand = "show"
        self.control = True
        self.orient = True
        self.ccball = 0
        
    def move(self, w):

        self.gravityd()
        self.now = datetime.datetime.now()
        self.second = self.now.second
        
        if self.animation > 3.8  and self.anim == "walk" and self.ccball == 0:
            self.animation = 0
            if self.animation < 10:
                self.sound1.play()
        if self.animation > 10.8 and self.anim == "fire":
            phy.showballen.append(showb.showballc(self.posx, self.posy, self.orientation))
            self.anim = "walk"
            self.animation = 0
        if self.anim == "fire":
            self.animation += 0.3
            

        
        global gravityconst
        key = pg.key.get_pressed()
    
        if key[pg.K_d] and self.control:
            self.posx += (w / 300) * self.speed
            self.orient = False
            if self.anim == "walk" and gravity < 1:
                self.animation += 0.3
            self.orientation = "right"
        elif key[pg.K_a] and self.control:
            self.orient = True
            self.posx -= (w / 300)* self.speed
            if self.anim == "walk"  and gravity < 1:
                self.animation += 0.3
            self.orientation = "left"
            
        elif key[pg.K_LSHIFT] and gravity == False and val.showinpen < val.maxshow:
            self.control = False
            self.ccball += 0.5
            if self.ccball > 99:
                self.ccball = 0
                #self.sound1.play()
                val.showinpen += 1
            if datetime.datetime.now().second % 2 == 0:
                self.animation = 11
            else:
                self.animation = 12
            val.coefcreate = self.ccball
        else:  
            val.coefcreate = self.ccball
            self.control = True
            self.ccball = 0  
        if key[pg.K_SPACE] and self.isJump == False and gravity == False:
            self.isJump = True
            gravityconst = 0
            self.anim = "jump"
            
        #print(self.second)
        if self.second < 1:
            self.oldsecond = 0.3
        if key[pg.K_RETURN] and self.second > self.oldsecond + 0.5 and val.showinpen > 0:
            self.oldsecond = self.second
            self.anim ="fire"
            self.animation = 7
          
        
            

    def jump(self):
        
        global gravity
        global gravityconst
        # Check if mario is jumping and then execute the
        # jumping code.
        if self.isJump:
            self.anim = "jump"
            if self.jumpCount >= 0:
                neg = 1 
                if self.jumpCount <= 11 and self.jumpCount >= 6:
                    self.animation = 4
                if self.jumpCount <= 5 and self.jumpCount >= 0:
                    self.animation = 5
                
                
                if self.jumpCount < 0:
                    neg = -1
                self.posy -= self.jumpCount**2 * 0.5 * neg
                self.jumpCount -= 1
            else:
                
                self.animation = 6   
                self.isJump = False
                self.jumpCount = 10

    def gravityd(self):
        global gravity
        global gravityconst
        if self.countgrav > 6:
            self.countgrav = 1
        if gravityconst < 6:
            gravityconst = self.countgrav
            self.countgrav = self.countgrav + 0.5

    
        

        

            

             
            
    def blit(self, win):
        win.blit(pg.transform.flip(self.image[int(self.animation)], self.orient, False), (self.posx, self.posy))
        
        
    # Check if mario is jumping and then execute the
    # jumping code.
               
                
                
                
            
    
    def standon(self, obj, vid):
        global gravity
        if vid == "plat" and self.posx + self.width / 1.3> obj.posx and self.posx + self.width / 4< obj.posx + obj.width and self.posy + self.height / 1.2  > obj.posy and self.posy + self.height / 1.6  < obj.posy:    
            return True
        elif vid == "ruby" and self.posx + self.width / 2  > obj.posx - (obj.width * 2) and self.posx < obj.posx - obj.width and self.posy + self.width > obj.posy and self.posy < obj.posy + obj.width:    
            return True   
        else:
            return False
        
        

ifcolplat = 0
gravityconst = 5
 
sound1 = pg.mixer.Sound('data/sound/money/ruby_1_1.wav')
def allpenguin(win, w, obj, list_platform, list_ruby):
    global time
    global gravity
    global ifcolplat
    global gravityconst
    obj.move(w) 
    obj.jump()
    time += 0.1
    if time == 10:
        time = 0
    for i in range(0, len(list_platform)):
        if obj.standon(list_platform[i], "plat"):
            gravity = False #574
            if obj.anim != "fire":
                obj.anim = "walk"
            obj.stand = "show"
        
        if obj.standon(list_platform[i], "plat") == False:
            ifcolplat += 1
            
    if ifcolplat ==  len(list_platform):
        gravity = True
   
    ifcolplat = 0        
    for i in range(0, len(list_ruby)):
        if obj.standon(list_ruby[i], "ruby"):
            log.line_ruby[log.level - 1][i] = 0
            list_ruby[i].posx += 10000
            sound1.play()
            if list_ruby[i].vids == "ruby_low":
                val.schore += 50
            elif list_ruby[i].vids == "ruby_middle":
                val.schore += 125
            elif list_ruby[i].vids == "ruby_big":
                val.schore += 250
            
           
            break
        
    obj.blit(win)
    if gravity == True:
        obj.posy += gravityconst

