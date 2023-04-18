import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_r = pg.transform.flip(bg_img, True, False)
    kt_img = pg.image.load("ex01/fig/3.png")
    kt_img_1 = pg.transform.flip(kt_img, True, False)
    kt_img_2 = pg.transform.rotozoom(kt_img_1,10,1.0)
    kt_img_3 = pg.transform.rotozoom(kt_img_1,8,1.0)
    kt_img_4 = pg.transform.rotozoom(kt_img_1,6,1.0)
    kt_img_5 = pg.transform.rotozoom(kt_img_1,4,1.0)
    kt_img_6 = pg.transform.rotozoom(kt_img_1,2,1.0)
    kt_list = [kt_img_1,kt_img_2,kt_img_3,kt_img_4,kt_img_5,kt_img_6]

    tmr = 0
    rev = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x =tmr%1600
        if x==1599:
            x=0
            if rev==0:
                rev = 1
            elif rev==1:
                rev = 0

        if rev==0:
            screen.blit(bg_img, [-x, 0])
            screen.blit(bg_img_r, [1600-x, 0])
        elif rev==1:
            screen.blit(bg_img_r, [-x, 0])
            screen.blit(bg_img, [1600-x, 0])
        if tmr%6==0:
            screen.blit(kt_list[0],[300,200])
        elif tmr%6==1:
            screen.blit(kt_list[1],[300,200])
        elif tmr%6==2:
            screen.blit(kt_list[2],[300,200])
        elif tmr%6==3:
            screen.blit(kt_list[3],[300,200])
        elif tmr%6==4:
            screen.blit(kt_list[4],[300,200])
        else:
            screen.blit(kt_list[5],[300,200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()