from dynamic import showball
#import sys
#sys.path.append('../')
import logicgame as log
showballen = []

imp = True

def main(win, scale):
    global imp
    if imp:
        showball.loadimage(scale)
        imp = False
    for i in range(len(showballen)):
        showballen[i].blitting(win)
        if showballen[i].destroy == True:
            del showballen[i]
            break
    for i in range(len(showballen)):
        for j in range(len(log.list_platforms)):
            showballen[i].collision(log.list_platforms[j], "platform")
        for b in range(len(log.hunt_list)):
            showballen[i].collision(log.hunt_list[b], "hunt")
    

