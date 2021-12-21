import pygame as pg

list_ruby = []
isimprotimage = True 
def importimage(cw, ch):
    global list_ruby
    list_ruby = [pg.image.load('data/money/low.png'), pg.image.load('data/money/middle.png'),pg.image.load('data/money/big.png')]
    for i in range(0, len(list_ruby)):
        list_ruby[i] = pg.transform.scale(list_ruby[i], (list_ruby[i].get_width() * cw , list_ruby[i].get_height() * ch))
        


class ruby():
    movev = True
    def __init__(self, px, py, setprocx, setprocy, vid):
            self.procx = px / 100
            self.procy = py / 100
            self.posx = self.procx * setprocx
            self.posy = self.procy * setprocy
           
            self.width = 10#self.rect.width
            self.vids = vid
            self.posyconst = self.posy
    def move(self):
        if self.posy > self.posyconst + 3:
            self.movev = False
        elif self.posy < self.posyconst - 3:
            self.movev = True
        if self.movev :
            self.posy += 1
        else:
            self.posy -=1


def defruby(win,  list_rubines,cw, ch,):
    global list_ruby
    global isimprotimage
   
    if isimprotimage:
        importimage(cw, ch)
        isimprotimage = False
    
    
        
    for i in range(0, len(list_rubines)):
        list_rubines[i].move()
        if list_rubines[i].vids == "ruby_low":
            win.blit(list_ruby[0], (list_rubines[i].posx, list_rubines[i].posy))
            list_rubines[i].width = list_ruby[0].get_rect().width
             
        elif list_rubines[i].vids == "ruby_middle":
            win.blit(list_ruby[1], (list_rubines[i].posx, list_rubines[i].posy))
            list_rubines[i].width = list_ruby[1].get_rect().width
        elif list_rubines[i].vids == "ruby_big":
            win.blit(list_ruby[2], (list_rubines[i].posx, list_rubines[i].posy))
            list_rubines[i].width = list_ruby[2].get_rect().width
        #list_ruby[0].fill((a, a, a), special_flags=pg.BLEND_RGB_ADD)
        

