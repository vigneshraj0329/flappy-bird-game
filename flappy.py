import pygame
import time
pygame.init()
width=393
height=946
screen=pygame.display.set_mode((width,height))
bg=pygame.image.load("back_g.png")
screen.blit(bg,(0,0))
pygame.display.update()

time.sleep(5)
pygame.quit()