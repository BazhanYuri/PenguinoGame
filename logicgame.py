import pygame as pg
from level import part_1
import values as val
import bullet_phy as bp
step = "Step_1"
level = 5
#createlevel
list_platforms = []
list_fd = []
jew_list = []
hunt_list = []

line_ruby = [[1, 1, 1]#1
,[1, 1, 1, 1]#2
,[1, 1, 1, 1, 1]#3
,[1, 1, 1, 1, 1]#4
,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]#5
,[1, 1, 1, 1, 1, 1]#6
,[1, 1, 1, 1]
,[1, 1, 1, 1, 1, 1]
,[1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1]
,[1, 1, 1, 1, 1]#10
,[1, 1, 1, 1, 1, 1, 1]
,[1, 1, 1, 1, 1, 1, 1, 1, 1]
,[1, 1, 1, 1, 1, 1, 1, 1, 1]
,[1, 1, 1, 1, 1, 1, 1, 1, 1]
,[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


is_hunt = [
    [3, 3]#level1
    ,[0]
    ,[0]
    ,[0]
    ,[0]
    ,[0]
    ,[3, 3]#level7
    ,[3, 3]#level8
    ,[3, 3, 3]#level9
    ,[3]#level10


]
def clear():
    list_platforms.clear()
    list_fd.clear()
    jew_list.clear()
    hunt_list.clear()
    bp.bullet_list.clear()
def create_level(w, h, constw, consth, obj):
    global step
    global level
    
    if step == "Step_1":
        obj.posy -= 20
        if level == 1:
            part_1.cs1l1(w, h, constw, consth)
        
        if level == 2:
            part_1.cs1l2(w, h, constw, consth)
        if level == 3:
            part_1.cs1l3(w, h, constw, consth)
        if level == 4:
            part_1.cs1l4(w, h, constw, consth)
            obj.posy = h * 0.55
        if level == 5:
            part_1.cs1l5(w, h, constw, consth)
            obj.posy = h * 0.55
        if level == 6:
            part_1.cs1l6(w, h, constw, consth)
            
        if level == 7:
            part_1.cs1l7(w, h, constw, consth)
        if level == 8:
            part_1.cs1l8(w, h, constw, consth)
        if level == 9:
            part_1.cs1l9(w, h, constw, consth)
        if level == 10:
            part_1.cs1l10(w, h, constw, consth)
        if level == 11:
            part_1.cs1l11(w, h, constw, consth)
        if level == 12:
            part_1.cs1l12(w, h, constw, consth)
        if level == 13:
            part_1.cs1l13(w, h, constw, consth)
        if level == 14:
            part_1.cs1l14(w, h, constw, consth)
        if level == 15:
            part_1.cs1l15(w, h, constw, consth)

            


    

def killpen(w, h, obj):
    if obj.posy > h:
        val.lifepen -= 1
        obj.posy -=  h / 3
        obj.posx =  w * 0.03
    
def logicgame(w, h, obj):
    killpen(w, h, obj)

def clearlists(obj, porm, w, h, constw, consth):
    global level
    
    clear()
    obj.posx = 0
    
    if porm:
        level += 1
        
    else:
        level -= 1
        obj.posx = w
    #obj.posy = h
    create_level(w, h, constw, consth,obj)
    
def defnextlevel(obj, w, h, constw, consth):
    global level
    global step
    if obj.posx > w and step == "Step_1":
        clearlists(obj, 1, w, h, constw, consth)
        
    
    if obj.posx < 0 and step == "Step_1":
        clearlists(obj, 0, w, h, constw, consth)
        
        