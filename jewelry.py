import pygame as pg

class jewelry:
    def __init__(self, px, py, cw, ch, setprocx, setprocy, vid):
        def __init__(self, px, py, cw, ch, setprocx, setprocy, vid):
            self.procx = px / 100
            self.procy = py / 100
            self.posx = self.procx * setprocx
            self.posy = self.procy * setprocy
            if vid == "ruby_1":
                self.image = pg.image.load('data/money/low.png')
            
            
            self.sizew, self.sizeh = self.image.get_width(), self.image.get_height()
            self.image = pg.transform.scale(self.image, (self.sizew * cw , self.sizeh * ch))
            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height