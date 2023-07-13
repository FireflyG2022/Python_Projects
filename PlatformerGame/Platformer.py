"""
Importing important libraries
"""
import pygame, sys
import random
"""
Setting up an environment to initialize pygame
"""
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Coin Mania')
szer = 600
wys = 600
window = pygame.display.set_mode((szer, wys),0,32)


#setting font settings
font = pygame.font.SysFont(None, 30)
class LavaPlatform():
    def __init__(self,x,y,szer,wys):
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.kolor = (250, 150, 27)
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
        self.czyMaByc = True
    def rysujLawe(self):
        if self.czyMaByc == True:
            pygame.draw.rect(window, self.kolor, self.obszar)
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
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.czyWidoczna = True
        self.kolor = (237,199,92)
        self.gracz = Player(50,150,32,32)

    def rysujMon(self):
        if self.czyWidoczna:
            pygame.draw.circle(window,self.kolor,(self.x, self.y) , self.r)

    def sprawdzZjadanie(self,obszar):

        if obszar.collidepoint(self.x,self.y) == True:
            self.czyWidoczna = False
            self.gracz.iloscMonet += 1
            print(self.gracz.iloscMonet)
            mainClock.tick(1000)
class Player():
    def __init__(self,x,y,szer,wys):
        self.x = x
        self.y = y
        self.szer = szer
        self.wys = wys
        self.obszar = pygame.Rect(self.x,self.y,self.szer,self.wys)
        self.grafika = pygame.image.load('kula.png')
        self.iloscMonet = 0
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



 
"""
A function that can be used to write text on our screen and buttons
"""
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:

        window.fill((0,190,255))
        draw_text('The coin mania', font, (0,0,0), window, 250, 40)
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)


        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                gameHard()
                gameHard()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        pygame.draw.rect(window, (255, 0, 0), button_2)
 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), window, 270, 115)
        draw_text('OPTIONS', font, (255,255,255), window, 250, 195)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(10)

"""
This function is called when the "PLAY" button is clicked.
"""
ShouldLavaBeVisible = True
def gameHard():
            running = True
            start = 1000
            score = 0
            score_inc = 1
            timer = pygame.time.Clock()
            draw_text('Ilosc monet', font, (0, 0, 0), window, 250, 40)
            while running:
               platformsList = []
               platformsList.append(Platform(100, 100, 150,20))
               platformsList.append(Platform(150, 300, 98,15))
               platformsList.append(Platform(200, 400, 50,50))
               platformsList.append(Platform(250, 250, 80,10))
               platformsList.append(Platform(350, 500, 44,33))
               platformsList.append(Platform(200, 175, 77,11))
               platformsList.append(Platform(0, 570, szer,30))
               platformsList.append(Platform(500,150,150,20))
               platformsList.append(Platform(300,430,100,20))
               platformsList.append(Platform(500,500,50,50))

               coinsList = [
                   pygame.Rect(100, 250, 23,23),
                   pygame.Rect(300,220,23,23),
                   pygame.Rect(200,90,23,23),
                   pygame.Rect(500,500,23,23),
                   pygame.Rect(500,100,23,23),
                   pygame.Rect(300,100,23,23),

               ]
               lawaList = []
               lawaList.append(LavaPlatform(190,570,560,600))

               gracz = Player(50,150,32,32)

               game_state = "start_menu"
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
                       for l in lawaList:
                           l.rysujLawe()
                           if gracz.obszar.colliderect(l.obszar) == True:
                               pygame.quit()
                               quit()
                       for c in coinsList:
                           pygame.draw.rect(window,'yellow',c)
                           if gracz.obszar.colliderect(c):
                               score += score_inc
                               print(score)
                               coinsList.remove(c)

                       if czyDotyka == False:
                           gracz.ruchDol()

                       if start == 0:
                            pygame.quit()
                            quit()

                       gracz.drawPlayer()
                       mainClock.tick(100000)
                       start -= 1
                       ile_monet_do_wygranej = 6
                       if score == ile_monet_do_wygranej:
                           draw_text("Wygrywasz, gratulacje", font, (255,255,255),window, szer/2,200)
                       draw_text(str(start), font, (255, 255, 255), window, 20, 40)
                       score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                       window.blit(score_text, (10, 10))
                       pygame.display.flip()


def gameEasy():
    running = True
    start = 1000
    score = 0
    score_inc = 1
    timer = pygame.time.Clock()
    draw_text('Ilosc monet', font, (0, 0, 0), window, 250, 40)
    while running:
        platformsList = []
        platformsList = []
        platformsList.append(Platform(100, 100, 150, 20))
        platformsList.append(Platform(150, 300, 98, 15))
        platformsList.append(Platform(200, 400, 50, 50))
        platformsList.append(Platform(250, 250, 80, 10))
        platformsList.append(Platform(350, 500, 44, 33))
        platformsList.append(Platform(200, 175, 77, 11))
        platformsList.append(Platform(0, 570, szer, 30))
        platformsList.append(Platform(500, 150, 150, 20))
        platformsList.append(Platform(300, 430, 100, 20))
        platformsList.append(Platform(500, 500, 50, 50))
        coinsList = [
            pygame.Rect(100, 250, 23, 23),
            pygame.Rect(300, 220, 23, 23),
            pygame.Rect(200, 90, 23, 23),
            pygame.Rect(500, 500, 23, 23),
            pygame.Rect(500, 100, 23, 23),
            pygame.Rect(300, 100, 23, 23),

        ]
        gracz = Player(50, 150, 32, 32)

        game_state = "start_menu"
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
                for c in coinsList:
                    pygame.draw.rect(window, 'yellow', c)
                    if gracz.obszar.colliderect(c):
                        score += score_inc
                        print(score)
                        coinsList.remove(c)

                if czyDotyka == False:
                    gracz.ruchDol()

                if start == 0:
                    pygame.quit()
                    quit()
                gracz.drawPlayer()
                mainClock.tick(100000)
                start -= 1
                ile_monet_do_wygranej = 6
                if score == ile_monet_do_wygranej:
                    draw_text("Wygrywasz, gratulacje", font, (255, 255, 255), window, szer / 2, 200)
                draw_text(str(start), font, (255, 255, 255), window, 20, 40)
                score_text = font.render(f'Score: {score}', True, (255, 255, 255))
                window.blit(score_text, (10, 10))
                pygame.display.flip()

"""
This function is called when the "OPTIONS" button is clicked.
"""
def options():
    running = True
    click = False
    while running:
        window.fill((0,190,255))
        mx, my = pygame.mouse.get_pos()
        draw_text('OPTIONS ', font, (255, 255, 255), window, 20, 20)
        draw_text('Choose game difficulty ', font, (255, 255, 255), window, 20, 40)
        button = pygame.Rect(10, 100, 200, 50)
        pygame.draw.rect(window, (255, 0, 0), button)
        draw_text('EASY ', font, (255, 255, 255), window, 50, 120)
        button_a = pygame.Rect(10,200,200,50)
        pygame.draw.rect(window,(255,0,0), button_a)
        draw_text('HARD ', font, (255, 255, 255), window, 50, 220)
        lawaa = LavaPlatform(0,570,150,200)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mainClock.tick(10)
        if button.collidepoint((mx,my)):
            if click:
                gameEasy()
        if button_a.collidepoint((mx,my)):
            if click:
                gameHard()

        pygame.display.update()
 
main_menu()
