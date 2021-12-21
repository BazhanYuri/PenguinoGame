import bullet_hunt as bul
bullet_list = []



def main(win, w, h, obj):
    if bul.isscale:
        bul.imagescale(w, h)
        bul.isscale = False
    if len(bullet_list) > 0:
        for i in range(0, len(bullet_list)):
            bullet_list[i].blitt(win)
            if bullet_list[i].shot(obj):
                del bullet_list[i]  
                break  
    