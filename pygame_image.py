import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kt_img = pg.image.load("ex01/fig/3.png")
    kt_img_1 = pg.transform.flip(kt_img, True, False)
    kt_img_2 = pg.transform.rotozoom(kt_img_1,10,1.0)
    kt_list = [kt_img_1,kt_img_2]
    x = 0

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x -=1
        if x==1599:
            x=0
        screen.blit(bg_img, [0+x, 0])
        screen.blit(bg_img, [1600+x, 0])
        if tmr%2==0:
            screen.blit(kt_list[0],[300,200])
        else:
            screen.blit(kt_list[1],[300,200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()