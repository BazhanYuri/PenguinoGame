import pygame 
import values as val
import penguin as pen
pygame.init()
imageinterface = []

def impimages(w):
    global imageinterface
    imageinterface = [pygame.image.load('data/interface/Showball.png'), pygame.image.load('data/interface/heart.png')]
    #for i in range(0, len(imageinterface)):
    imageinterface[0] = pygame.transform.scale(imageinterface[0], (int(w * 0.03),int(w * 0.03)))
    imageinterface[1] = pygame.transform.scale(imageinterface[1], (int(w * 0.03),int(w * 0.03)))



f1 = pygame.font.Font('data/fonts/font_pixel.ttf', 72)
textScore = f1.render("Score " + str(val.schore), True,(0, 0, 200))



def showball(win, w, h):
    spox = 0.6
    for i in range(0, val.showinpen):
        win.blit(imageinterface[0], (w * spox, h * 0.03))
        spox += 0.03

textScore2 = f1.render("Score " + str(val.coefcreate), True,(0, 0, 200))
def createshow(win, w, h):
    pygame.draw.rect(win, (255, 255, 255) , (w * 1.6, h * 0.1, 100 * w * 0.004 , 10))

    pygame.draw.rect(win, (0, 255 - int(val.coefcreate) * 2.5, int(val.coefcreate) * 2.5) , (w * 1.6, h * 0.1, int(val.coefcreate) * w * 0.004    , 10))

    #textScore2 = f1.render("Score " + str(), True,(0, 0, 200))
    #win.blit(textScore2, (, ))

def showheart(win, w, h):
    spox = 0.5
    for i in range(0, val.lifepen):
        win.blit(imageinterface[1], (w * spox, h * 0.03))
        spox += 0.03


impbool = True
def main(win, w, h):
    global impbool
    if impbool:
        impimages(w)
        impbool = False
    showball(win, w, h)
    showheart(win, w, h)
    textScore = f1.render("Score " + str(val.schore), True,(0, 0, 200))
    win.blit(textScore, (w * 0.78, h * 0.03))
    createshow(win, w* 0.38, h)
    

    
    