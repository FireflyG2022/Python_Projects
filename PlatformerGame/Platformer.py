
import pygame
import random

pygame.init()

szer = 600
wys = 600

window = pygame.display.set_mode((szer,wys))

class Platform():
    def __init__(self,x,y, szer,wys):
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.kolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255) )
        self.obszar = pygame.Rect(self.x, self.y, self.szer, self.wys)
    def rysujPlat(self):
        pygame.draw.rect(window,self.kolor,self.obszar)
class Coin():
    def __init__(self,x,y,r,):
        self.x = x
        self.y = y
        self.r = r
    def rysujMon(self):
        pygame.draw.circle(window,(237, 199, 92),(self.x, self.y) , self.r)

platformsList = []
platformsList.append(Platform(100, 100, 150,20))
platformsList.append(Platform(150, 300, 98,15))
platformsList.append(Platform(200, 400, 50,50))
platformsList.append(Platform(250, 250, 80,10))
platformsList.append(Platform(350, 500, 44,33))
platformsList.append(Platform(200, 175, 77,11))
platformsList.append(Platform(0, 570, szer,30))
coinsList = []
coinsList.append(Coin(110, 200, 10))
coinsList.append(Coin(200, 10, 10))
coinsList.append(Coin(10, 570, 5))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for p in platformsList:
        p.rysujPlat()
    for c in coinsList:
        c.rysujMon()
    pygame.display.update()
