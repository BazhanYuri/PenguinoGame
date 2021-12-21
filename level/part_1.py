import platforms as pl
import fdecor as fd
import ruby as ru
import hunter as hunt
import logicgame as log




    
def cs1l1(w, h, constw, consth):
    #platform
    log.list_platforms.append(pl.platform(w, h, constw, consth, -2, 75, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 34, 75,  "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 65, 75,  "usuall", False))
    
    #decor_front
    log.list_fd.append(fd.decorfront(w, h, constw, consth, 14, 38, "spruce_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 67, 40, "spruce_2"))

    #list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 40, 65, "bush_1"))
    #list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 70, 65, "bush_2"))
    
    #ruby
    if log.line_ruby[0][0]:
        log.jew_list.append(ru.ruby(w, h, 30, 70, "ruby_low"))
    if log.line_ruby[0][1]:
        log.jew_list.append(ru.ruby(w, h, 60, 60, "ruby_low"))
    if log.line_ruby[0][2]:
        log.jew_list.append(ru.ruby(w, h, 90, 70, "ruby_low"))
    
    #hunter
    
    log.hunt_list.append(hunt.hunter(w, h, 50, 65, w * 0.1, log.is_hunt[0][0], 0))
    log.hunt_list.append(hunt.hunter(w, h, 30, 65, w * 0.2, log.is_hunt[0][1], 1))

def cs1l2(w, h, constw, consth):
    #platform
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -2, 75, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 50, 75, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 70, 75, "usuall", False))

    #decor_front
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 14, 67, "bush_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 84, 38, "spruce_1"))
    #ruby
    if log.line_ruby[1][0]:
        log.jew_list.append(ru.ruby(w, h, 30, 70, "ruby_low"))
    if log.line_ruby[1][1]:
        log.jew_list.append(ru.ruby(w, h, 60, 60, "ruby_low"))
    if log.line_ruby[1][2]:
        log.jew_list.append(ru.ruby(w, h, 55, 70, "ruby_low"))
    
    if log.line_ruby[1][3]:
        log.jew_list.append(ru.ruby(w, h, 75, 70, "ruby_low"))
    
    

def cs1l3(w, h, constw, consth):
    #platform
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -2, 75, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 34, 85,  "usuall", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 70, 65,  "usuall", False))
    #decor_front
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 14, 67, "bush_1"))
    log.list_fd.append(fd.decorfront(w, h, constw, 123, 54, 48, "spruce_1"))
    #ruby
    if log.line_ruby[2][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 70, "ruby_low"))
    if log.line_ruby[2][1]:
        log.jew_list.append(ru.ruby(w, h, 50, 80, "ruby_low"))
    if log.line_ruby[2][2]:
        log.jew_list.append(ru.ruby(w, h, 65, 45, "ruby_low"))
    if log.line_ruby[2][3]:
        log.jew_list.append(ru.ruby(w, h, 60, 50, "ruby_middle"))
    if log.line_ruby[2][4]:
        log.jew_list.append(ru.ruby(w, h, 85, 60, "ruby_low"))
    
    


def cs1l4(w, h, constw, consth):
    #platform
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -2, 65, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 34, 78,  "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 65, 85,  "usuall", False))

    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 40, 61.5,  "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 75, 68.5,  "3on2", True))
    #decor_front
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 10, 28, "spruce_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 40, 43, "spruce_2"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 76, 63, "bush_3"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 83, 63.5, "bush_2"))
    #ruby
    if log.line_ruby[3][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 60, "ruby_low"))
    if log.line_ruby[3][1]:
        log.jew_list.append(ru.ruby(w, h, 30, 40, "ruby_low"))
    if log.line_ruby[3][2]:
        log.jew_list.append(ru.ruby(w, h, 60, 45, "ruby_low"))
    if log.line_ruby[3][3]:
        log.jew_list.append(ru.ruby(w, h, 50, 75, "ruby_low"))
    if log.line_ruby[3][4]:
        log.jew_list.append(ru.ruby(w, h, 75, 45, "ruby_low"))
    
def cs1l5(w, h, constw, consth):
    #platform
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -10, 75, "usuall", False))
    
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 65, 85,  "usuall", False))

    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 10, 58.5,  "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 14, 42,  "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 75, 68.5,  "3on2", True))

    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 45, 67,  "3on4", False))

    #decor
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 10, 38, "spruce_1"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 47, 32, "spruce_2"))
    #ruby
    if log.line_ruby[4][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 55, "ruby_low"))
    if log.line_ruby[4][1]:
        log.jew_list.append(ru.ruby(w, h, 20, 25, "ruby_low"))
    if log.line_ruby[4][2]:
        log.jew_list.append(ru.ruby(w, h, 23, 25, "ruby_low"))
    if log.line_ruby[4][3]:
        log.jew_list.append(ru.ruby(w, h, 35, 35, "ruby_low"))
    if log.line_ruby[4][4]:
        log.jew_list.append(ru.ruby(w, h, 35, 45, "ruby_middle"))
    if log.line_ruby[4][5]:
        log.jew_list.append(ru.ruby(w, h, 33, 65, "ruby_middle"))
    if log.line_ruby[4][6]:
        log.jew_list.append(ru.ruby(w, h, 65, 45, "ruby_low"))
    if log.line_ruby[4][7]:
        log.jew_list.append(ru.ruby(w, h, 80, 80, "ruby_low"))
    if log.line_ruby[4][8]:
        log.jew_list.append(ru.ruby(w, h, 90, 80, "ruby_low"))
    if log.line_ruby[4][9]:
        log.jew_list.append(ru.ruby(w, h, 96, 40, "ruby_low"))
   
def cs1l6(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -20, 85, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 24, 80, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth),47, 90, "3on2", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 72, 85, "usuall", False))
    #decor
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 3, 79, "fence_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth),25, 74, "fence_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth),82, 78, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth),88, 78, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth),85, 70, "box_1"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 48, 53, "spruce_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 73, 77, "bush_1"))


    if log.line_ruby[5][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 65, "ruby_low"))
    if log.line_ruby[5][1]:
        log.jew_list.append(ru.ruby(w, h, 35, 76, "ruby_low"))
    if log.line_ruby[5][2]:
        log.jew_list.append(ru.ruby(w, h, 40, 55, "ruby_low"))
    if log.line_ruby[5][3]:
        log.jew_list.append(ru.ruby(w, h, 43, 58, "ruby_middle"))
    if log.line_ruby[5][4]:
        log.jew_list.append(ru.ruby(w, h, 53, 63, "ruby_low"))
    if log.line_ruby[5][5]:
        log.jew_list.append(ru.ruby(w, h, 67, 63, "ruby_low"))
   
    
    

def cs1l7(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -5, 85, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 32, 70, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 50,99, "3on2", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 63, 80, "usuall", False))

    #decor
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 10, 48, "spruce_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 80, 45, "spruce_2"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 62, 74, "bush_2"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 87, 72, "bush_1"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 23, 78, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 4, 79, "fence_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 35, 43, "tower_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 65, 43, "tower_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 50, 96, "boat_1"))

    

    if log.line_ruby[6][0]:
        log.jew_list.append(ru.ruby(w, h, 24, 45, "ruby_low"))
    if log.line_ruby[6][1]:
        log.jew_list.append(ru.ruby(w, h, 35, 45, "ruby_low"))
    if log.line_ruby[6][2]:
        log.jew_list.append(ru.ruby(w, h, 75, 45, "ruby_low"))
    if log.line_ruby[6][3]:
        log.jew_list.append(ru.ruby(w, h, 60, 74, "ruby_big"))
    
    #hunter
    log.hunt_list.append(hunt.hunter(w, h, 30, 59, w * 0.3, log.is_hunt[6][0], 0))
    log.hunt_list.append(hunt.hunter(w, h, 36, 59, w * 0.3, log.is_hunt[6][1], 1))


def cs1l8(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -20, 80, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 30, 75, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 55, 75, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 80, 75, "usuall", False))


    #decor 
    
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 39, 69, "bush_2"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 31, 37, "spruce_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 7, 72, "bush_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 12, 73, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 78, 73, "boat_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 85, 69, "fence_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 95, 67, "bush_1"))


    if log.line_ruby[7][0]:
        log.jew_list.append(ru.ruby(w, h, 21, 73, "ruby_low"))
    if log.line_ruby[7][1]:
        log.jew_list.append(ru.ruby(w, h, 33, 48, "ruby_low"))
    if log.line_ruby[7][2]:
        log.jew_list.append(ru.ruby(w, h, 47, 67, "ruby_middle"))
    if log.line_ruby[7][3]:
        log.jew_list.append(ru.ruby(w, h, 53, 67, "ruby_middle"))
    if log.line_ruby[7][4]:
        log.jew_list.append(ru.ruby(w, h, 64, 45, "ruby_low"))
    if log.line_ruby[7][5]:
        log.jew_list.append(ru.ruby(w, h, 76, 57, "ruby_middle"))
    #hunter
    log.hunt_list.append(hunt.hunter(w, h, 28, 64, w * 0.1, log.is_hunt[7][0], 0))
    log.hunt_list.append(hunt.hunter(w, h, 80, 64, w * 0.1, log.is_hunt[7][1], 1))

def cs1l9(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -1, 75, "3on4", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 25, 70, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 53, 85, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 70, 80, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 80, 31, "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 80, 47, "3on4", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 72, 64, "3on2", True))


    #decor
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 80, 5, "tower_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 87, 23, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 87, 23, "box_1"))
    #
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 80, 4, "tower_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 87, 23, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 87, 23, "box_1"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 26, 62, "bush_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 30, 64, "bush_2"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 36, 64, "bush_3"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 47, 63, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 53, 63, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 50, 56, "box_1"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 80, 43, "spruce_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 72, 27, "spruce_1"))
    
    
    if log.line_ruby[8][0]:
        log.jew_list.append(ru.ruby(w, h, 33, 65, "ruby_low"))
    if log.line_ruby[8][1]:
        log.jew_list.append(ru.ruby(w, h, 37, 55, "ruby_low"))
    if log.line_ruby[8][2]:
        log.jew_list.append(ru.ruby(w, h, 42, 45, "ruby_low"))
    if log.line_ruby[8][3]:
        log.jew_list.append(ru.ruby(w, h, 47, 55, "ruby_low"))
    if log.line_ruby[8][4]:
        log.jew_list.append(ru.ruby(w, h, 52, 65, "ruby_low"))
    if log.line_ruby[8][5]:
        log.jew_list.append(ru.ruby(w, h, 57, 75, "ruby_low"))
    if log.line_ruby[8][6]:
        log.jew_list.append(ru.ruby(w, h, 73, 60, "ruby_low"))
    if log.line_ruby[8][7]:
        log.jew_list.append(ru.ruby(w, h, 77, 51, "ruby_low"))
    if log.line_ruby[8][8]:
        log.jew_list.append(ru.ruby(w, h, 81, 42, "ruby_low"))
    if log.line_ruby[8][9]:
        log.jew_list.append(ru.ruby(w, h, 90, 42, "ruby_low"))
    if log.line_ruby[8][10]:
        log.jew_list.append(ru.ruby(w, h, 60, 35, "ruby_big"))
    if log.line_ruby[8][11]:
        log.jew_list.append(ru.ruby(w, h, 92, 76, "ruby_middle"))
    
    #hunter
    log.hunt_list.append(hunt.hunter(w, h, 24, 59, w * 0.3, log.is_hunt[8][0], 0))
    log.hunt_list.append(hunt.hunter(w, h, 36, 59, w * 0.2, log.is_hunt[8][1], 1))
    log.hunt_list.append(hunt.hunter(w, h, 50, 74, w * 0.13, log.is_hunt[8][2], 2))
def cs1l10(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -3, 80, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 15, 67, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 35, 56, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 75, 67, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 90, 80, "3on4", False))

    #decor
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 52, 30, "tower_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 22, 60, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 16, 60, "box_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 76, 64, "boat_1"))
    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 85, 59, "bush_1"))

    log.list_fd.append(fd.decorfront(w, h, int(constw), int(consth), 37, 18, "spruce_1"))


    if log.line_ruby[9][0]:
        log.jew_list.append(ru.ruby(w, h, 7, 60, "ruby_low"))
    if log.line_ruby[9][1]:
        log.jew_list.append(ru.ruby(w, h, 23, 45, "ruby_low"))
    if log.line_ruby[9][2]:
        log.jew_list.append(ru.ruby(w, h, 47, 30, "ruby_low"))
    if log.line_ruby[9][3]:
        log.jew_list.append(ru.ruby(w, h, 80, 45, "ruby_low"))
    if log.line_ruby[9][0]:
        log.jew_list.append(ru.ruby(w, h, 95, 70, "ruby_low"))
    #hunter
    log.hunt_list.append(hunt.hunter(w, h, 34, 45, w * 0.31, log.is_hunt[9][0], 0))

def cs1l11(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -3, 80, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 20, 70, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 70, 65, "usuall", False))

    if log.line_ruby[10][0]:
        log.jew_list.append(ru.ruby(w, h, 7, 50, "ruby_big"))
    if log.line_ruby[10][1]:
        log.jew_list.append(ru.ruby(w, h, 30, 60, "ruby_low"))
    if log.line_ruby[10][2]:
        log.jew_list.append(ru.ruby(w, h, 40, 60, "ruby_low"))
    if log.line_ruby[10][3]:
        log.jew_list.append(ru.ruby(w, h, 50, 60, "ruby_low"))
    if log.line_ruby[10][4]:
        log.jew_list.append(ru.ruby(w, h, 65, 40, "ruby_big"))
    if log.line_ruby[10][5]:
        log.jew_list.append(ru.ruby(w, h, 85, 60, "ruby_middle"))
    if log.line_ruby[10][6]:
        log.jew_list.append(ru.ruby(w, h, 95, 60, "ruby_middle"))

def cs1l12(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -3, 68, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 20, 60, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 70, 85, "usuall", False))

    if log.line_ruby[11][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 45, "ruby_low"))
    if log.line_ruby[11][1]:
        log.jew_list.append(ru.ruby(w, h, 18, 42, "ruby_middle"))
    if log.line_ruby[11][2]:
        log.jew_list.append(ru.ruby(w, h, 30, 35, "ruby_low"))
    if log.line_ruby[11][3]:
        log.jew_list.append(ru.ruby(w, h, 33, 31, "ruby_middle"))
    if log.line_ruby[11][4]:
        log.jew_list.append(ru.ruby(w, h, 45, 35, "ruby_low"))
    if log.line_ruby[11][5]:
        log.jew_list.append(ru.ruby(w, h, 48, 31, "ruby_middle"))
    if log.line_ruby[11][6]:
        log.jew_list.append(ru.ruby(w, h, 68, 61, "ruby_low"))
    if log.line_ruby[11][7]:
        log.jew_list.append(ru.ruby(w, h, 78, 77, "ruby_low"))
    if log.line_ruby[11][8]:
        log.jew_list.append(ru.ruby(w, h, 88, 77, "ruby_low"))


def cs1l13(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -3, 85, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 20, 80, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 40, 80, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 60, 80, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 83, 85, "usuall", False))

    if log.line_ruby[12][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 70, "ruby_low"))
    if log.line_ruby[12][1]:
        log.jew_list.append(ru.ruby(w, h, 26, 76, "ruby_low"))
    if log.line_ruby[12][2]:
        log.jew_list.append(ru.ruby(w, h, 37, 65, "ruby_low"))
    if log.line_ruby[12][3]:
        log.jew_list.append(ru.ruby(w, h, 46, 76, "ruby_low"))
    if log.line_ruby[12][4]:
        log.jew_list.append(ru.ruby(w, h, 57, 65, "ruby_low"))
    if log.line_ruby[12][5]:
        log.jew_list.append(ru.ruby(w, h, 66, 76, "ruby_low"))
    if log.line_ruby[12][6]:
        log.jew_list.append(ru.ruby(w, h, 77, 65, "ruby_low"))
    if log.line_ruby[12][7]:
        log.jew_list.append(ru.ruby(w, h, 92, 79, "ruby_middle"))

def cs1l14(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -3, 85, "3on4", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 35, 21, "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -8, 51, "3on2", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 35, 37, "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 35, 53, "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 35, 69, "3on2", True))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 15, 85, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 90, 85, "3on4", False))

    if log.line_ruby[13][0]:
        log.jew_list.append(ru.ruby(w, h, 3, 45, "ruby_big"))
    if log.line_ruby[13][1]:
        log.jew_list.append(ru.ruby(w, h, 25, 78, "ruby_low"))
    if log.line_ruby[13][2]:
        log.jew_list.append(ru.ruby(w, h, 57, 78, "ruby_middle"))
    if log.line_ruby[13][3]:
        log.jew_list.append(ru.ruby(w, h, 58, 63, "ruby_low"))
    if log.line_ruby[13][4]:
        log.jew_list.append(ru.ruby(w, h, 60, 43, "ruby_low"))
    if log.line_ruby[13][5]:
        log.jew_list.append(ru.ruby(w, h, 75, 55, "ruby_middle"))
    if log.line_ruby[13][6]:
        log.jew_list.append(ru.ruby(w, h, 80, 55, "ruby_middle"))
    if log.line_ruby[13][7]:
        log.jew_list.append(ru.ruby(w, h, 80, 50, "ruby_low"))
    if log.line_ruby[13][8]:
        log.jew_list.append(ru.ruby(w, h, 80, 60, "ruby_low"))


def cs1l15(w, h, constw, consth):
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), -2, 85, "usuall", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 45, 85, "3on2", False))
    log.list_platforms.append(pl.platform(w, h, int(constw), int(consth), 70, 85, "usuall", False))

    if log.line_ruby[14][0]:
        log.jew_list.append(ru.ruby(w, h, 15, 80, "ruby_low"))
    if log.line_ruby[14][1]:
        log.jew_list.append(ru.ruby(w, h, 20, 80, "ruby_low"))
    if log.line_ruby[14][2]:
        log.jew_list.append(ru.ruby(w, h, 25, 80, "ruby_low"))
    if log.line_ruby[14][3]:
        log.jew_list.append(ru.ruby(w, h, 30, 80, "ruby_low"))
    if log.line_ruby[14][4]:
        log.jew_list.append(ru.ruby(w, h, 35, 80, "ruby_low"))
    if log.line_ruby[14][5]:
        log.jew_list.append(ru.ruby(w, h, 41, 70, "ruby_middle"))
    if log.line_ruby[14][6]:
        log.jew_list.append(ru.ruby(w, h,52, 70, "ruby_big"))
    if log.line_ruby[14][7]:
        log.jew_list.append(ru.ruby(w, h, 63, 70, "ruby_middle"))
    if log.line_ruby[14][8]:
        log.jew_list.append(ru.ruby(w, h,52, 77, "ruby_low"))
    if log.line_ruby[14][9]:
        log.jew_list.append(ru.ruby(w, h,75, 80, "ruby_middle"))
    if log.line_ruby[14][10]:
        log.jew_list.append(ru.ruby(w, h,78, 80, "ruby_big"))
    if log.line_ruby[14][11]:
        log.jew_list.append(ru.ruby(w, h,82, 80, "ruby_low"))
    if log.line_ruby[14][12]:
        log.jew_list.append(ru.ruby(w, h,85, 80, "ruby_low"))
    