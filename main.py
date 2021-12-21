import pygame as pg
import penguin as pen
import platforms as pl
import logicgame as log
import fdecor as fd
import ruby as rb
import time
import background as bg
from level import part_1
from dynamic import physic as phy
import interface as inter
import hunter
import bullet_phy as bulp
pg.display.init()
pg.init()
winw = 1600
winh = 900
win = pg.display.set_mode((winw, winh), pg.FULLSCREEN)
clock = pg.time.Clock()

w, h = pg.display.get_surface().get_size()
constw = 3.333 / (1600 / w)
consth = 3.333 / (900 /h)

objpenguin = pen.penguin(w, h, constw, consth)



log.create_level(w, h, constw, consth, objpenguin)

seconds = time.time()

pg.mixer.music.load('data/sound/music/background.mp3')
pg.mixer.music.play()
pg.mixer.music.set_volume(0.15)

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT or i.type == pg.key :
            pg.quit()
    
    bg.background(win, w, h)
    

    pl.platformdef(win, log.list_platforms, constw, consth)
    log.logicgame(w, h, objpenguin)
    
    
    pen.allpenguin(win, w, objpenguin, log.list_platforms, log.jew_list)
    if len(phy.showballen):
        phy.main(win, int(constw))
    hunter.main(win, int(constw), int(consth), log.hunt_list, objpenguin)

    bulp.main(win, w, h, objpenguin)


    log.defnextlevel(objpenguin, w, h, constw, consth)
    
    rb.defruby(win, log.jew_list, int(constw), int(consth))
    
    fd.defdecorfront(win, log.list_fd, constw, consth )
    inter.main(win, w, h)
    
    pg.display.update()
    
    
    clock.tick(60)

    
    print(w, h)
    print("Seconds since epoch =", clock)	
