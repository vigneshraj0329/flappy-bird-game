import pygame
import time
pygame.init()
width=393
height=946
screen=pygame.display.set_mode((width,height))
bg=pygame.image.load("back_g.png")
screen.blit(bg,(0,0))
hero=pygame.image.load("bird.png")
hero1=pygame.transform.scale(hero,(80,60))
screen.blit(hero1,(25,450))

pygame.display.update()

time.sleep(5)
pygame.quit()