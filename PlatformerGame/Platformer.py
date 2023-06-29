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
        self.czyWidoczna = True
        self.kolor = (237,199,92)
    def rysujMon(self):
        if self.czyWidoczna:
            pygame.draw.circle(window,self.kolor,(self.x, self.y) , self.r)
    def sprawdzZjadanie(self,obszar):
        if obszar.collidepoint(self.x,self.y) == True:
            self.czyWidoczna = False
class Player():
    def __init__(self,x,y,szer,wys):
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
        self.grafika = pygame.image.load('kula.png')
    def drawPlayer(self):
        window.blit(self.grafika,(self.x,self.y))
    def ruchLewa(self):
        self.x = self.x - 5
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
    def ruchPrawa(self):
        self.x = self.x + 5
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
    def ruchDol(self):
        self.y = self.y + 5
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
    def ruchGora(self):
        self.y = self.y - 10
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
        

platformsList = []
platformsList.append(Platform(100, 100, 150,20))
platformsList.append(Platform(150, 300, 98,15))
platformsList.append(Platform(200, 400, 50,50))
platformsList.append(Platform(250, 250, 80,10))
platformsList.append(Platform(350, 500, 44,33))
platformsList.append(Platform(200, 175, 77,11))
platformsList.append(Platform(0, 570, szer,30))
coinsList = []
coinsList.append(Coin(150, 70, 15))
coinsList.append(Coin(300, 220, 15))

gracz = Player(50,150,32,32)

ile_na_skok = 0
ruchLewoAktywny = False
ruchPrawoAktywny = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ruchLewoAktywny = True
            if event.key == pygame.K_RIGHT:
                ruchPrawoAktywny = True
            if event.key == pygame.K_UP:
                ile_na_skok = 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ruchLewoAktywny = False
            if event.key == pygame.K_RIGHT:
                ruchPrawoAktywny = False
    window.fill('black')
    if ile_na_skok > 0:
        gracz.ruchGora()
        ile_na_skok = ile_na_skok - 1
    if ruchLewoAktywny == True:
        gracz.ruchLewa()
    if ruchPrawoAktywny == True:
        gracz.ruchPrawa()
    czyDotyka = False
    for p in platformsList:
        p.rysujPlat()
        if gracz.obszar.colliderect(p.obszar) == True:
            czyDotyka = True
    if czyDotyka == False:
        gracz.ruchDol()
    czySaMonety = False
    for c in coinsList:
        c.rysujMon()
        c.sprawdzZjadanie(gracz.obszar)
        if c.czyWidoczna == True:
            czySaMonety = True
    if czySaMonety == False:
        czcionka = pygame.font.SysFont("Arial", 25)
        obraz_napisu = czcionka.render("Brawo, wygrywasz!", 1, 'red')
        window.blit(obraz_napisu, (szer/2, 200))
    gracz.drawPlayer()
    pygame.time.wait(10)
    pygame.display.update()
