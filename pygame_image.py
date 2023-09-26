import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    rg_img = pg.image.load("ex01/fig/3.png")
    rg_img = pg.transform.flip(rg_img, True, False)
    rg_img2 = pg.transform.rotozoom(rg_img, 10, 1.0)
    rg_imgs = [rg_img, rg_img2]
    bg_imgs = pg.transform.flip(bg_img,True, False)
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_imgs,[1600-x,0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(rg_imgs[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()