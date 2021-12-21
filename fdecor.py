import pygame as pg

list_image_tree = []
list_image_bush = []
list_image_hunter = []

isloadimage = True
def imprimage(cw, ch):
    global list_image_tree
    global list_image_bush
    global list_image_hunter
    list_image_tree = [pg.image.load('data/fdecor/spruce_1.png'), pg.image.load('data/fdecor/spruce_2.png')]
    list_image_bush = [pg.image.load('data/fdecor/bush_1.png'), pg.image.load('data/fdecor/bush_2.png'), pg.image.load('data/fdecor/bush_3.png')]
    list_image_hunter = [pg.image.load('data/fdecor/fence_1.png'), pg.image.load('data/fdecor/tower_1.png')
    , pg.image.load('data/fdecor/boat_1.png'), pg.image.load('data/fdecor/box_1.png')]
    for i in range(0, len(list_image_tree) ):
        list_image_tree[i] = pg.transform.scale(list_image_tree[i], (int(list_image_tree[i].get_width() * cw), int(list_image_tree[i].get_height() * ch)))
    for i in range(0, len(list_image_bush) ):
        list_image_bush[i] = pg.transform.scale(list_image_bush[i], (int(list_image_bush[i].get_width() * cw), int(list_image_bush[i].get_height() * ch)))
    for i in range(0, len(list_image_hunter) ):
        list_image_hunter[i] = pg.transform.scale(list_image_hunter[i], (int(list_image_hunter[i].get_width() * cw), int(list_image_hunter[i].get_height() * ch)))

class decorfront():           
    def __init__(self, px, py, cw, ch, setprocx, setprocy, vid):
        self.procx = px / 100
        self.procy = py / 100
        self.posx = self.procx * setprocx
        self.posy = self.procy * setprocy
        self.vids = vid
        
        
        
       

def defdecorfront(win, decorfront, cw, ch):
    global list_image_tree
    global list_image_bush
    global isloadimage
    if isloadimage:
        imprimage(cw, ch)
        isloadimage = False
    for i in range(0, len(decorfront)):
        if decorfront[i].vids == "spruce_1":
            win.blit(list_image_tree[0], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "spruce_2":
            win.blit(list_image_tree[1], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "bush_1":
            win.blit(list_image_bush[0], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "bush_2":
            win.blit(list_image_bush[1], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "bush_3":
            win.blit(list_image_bush[2], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "fence_1":
            win.blit(list_image_hunter[0], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "tower_1":
            win.blit(list_image_hunter[1], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "boat_1":
            win.blit(list_image_hunter[2], (decorfront[i].posx, decorfront[i].posy))
        elif decorfront[i].vids == "box_1":
            win.blit(list_image_hunter[3], (decorfront[i].posx, decorfront[i].posy))        
        
