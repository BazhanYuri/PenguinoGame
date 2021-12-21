import pygame as pg
list_image_platform = []
isimpimageplatform = True

list_image_platform = []
def createimage(cw, ch):
    global list_image_platform
    list_image_platform = [pg.image.load('data/platforms/platform_1.png'), pg.image.load('data/platforms/platform3on4.png')
    , pg.image.load('data/platforms/platform3on2.png')]
    for i in range(0, len(list_image_platform)):
        list_image_platform[i] = pg.transform.scale(list_image_platform[i], (int(list_image_platform[i].get_width() * cw) , int(list_image_platform[i].get_height() * ch)))
class platform():
    global list_image_platform
    def __init__(self, px, py, cw, ch, setprocx, setprocy, vid, back):
        self.procx = px / 100
        self.procy = py / 100
        self.posx = self.procx * setprocx
        self.posy = self.procy * setprocy
        #self.image = pg.image.load('data/platforms/platform_1.png')
        #self.sizew, self.sizeh = self.image.get_width(), self.image.get_height()
        #self.image = pg.transform.scale(self.image, (self.sizew * cw , self.sizeh * ch))
        #self.rect = list_image_platform[0].get_rect()
        self.width = 100#self.rect.width
        self.height = 100
        self.vids = vid
        self.back = back
            

def platformdef(win, platform, cw, ch):
    global isimpimageplatform
    global list_image_platform
    if isimpimageplatform:
        createimage(cw, ch)
        isimpimageplatform = False
    for i in range(0, len(platform)):
        if platform[i].vids == "usuall":
          
            
            

            win.blit(list_image_platform[0], (platform[i].posx, platform[i].posy))
            platform[i].width = list_image_platform[0].get_rect().width
            platform[i].height = list_image_platform[0].get_rect().height
        if platform[i].vids == "3on4":
            win.blit(list_image_platform[1], (platform[i].posx, platform[i].posy))
            platform[i].width = list_image_platform[1].get_rect().width
            platform[i].height = list_image_platform[0].get_rect().height
        if platform[i].vids == "3on2":
            win.blit(list_image_platform[2], (platform[i].posx, platform[i].posy))
            platform[i].width = list_image_platform[2].get_rect().width
            platform[i].height = list_image_platform[0].get_rect().height
