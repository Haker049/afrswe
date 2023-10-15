from pygame import *
from random import randint
from time import sleep
window = display.set_mode((700,500))
display.init()
display.set_caption('За Домбасс!')
background = transform.scale(image.load('36.jpg'),(700,500))
miss = 0
point = 0

class GameSprite(sprite.Sprite):
    def __init__(self,speed,ima,x,y):
        super().__init__()
        self.image = transform.scale(image.load(ima),(90,90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class GG(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x < 700 - 60:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        global fire    
        fire = self.rect.x 



class gnids(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(90,610)
            self.rect.y = 0
            self.speed = randint(2,3)
            global miss 
            miss += 1

class ratatata(GameSprite):
    def update(self): 
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            ratatata.kill(self)
            global kolvo
            kolvo -= 1


hero = GG(5,'cnfk.png',300,400)
pyli = sprite.Group()
mrasi = sprite.Group()
for i in range(5):
    mrasi.add(gnids(randint(2,3), 'pngaaa.com-671148.png', randint(90,610),0))
    

kolvo = 0

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

clock = time.Clock()
FPS = 60
dombass = True
finish = False
nanax = mixer.Sound('fire.ogg')
winner = mixer.Sound('Gimny_-_Gosudarstvennyjj_gimn_SSSR_48240987.mp3')
loser = mixer.Sound('Ёбаный рот этого казино, блядь! Ты кто такой, сука! (256  kbps).mp3')
font.init()
font = font.SysFont('Arial', 20)

while dombass == True:
    for i in event.get():
        if i.type ==QUIT:
            dombass = False
        elif i.type ==KEYDOWN:
            if i.key == K_SPACE:
                if kolvo <=5:
                    pyli.add(ratatata(4,'bullet.png',fire,450)) 
                    kolvo += 1
                    nanax.play()
    if finish != True:
        window.blit(background,(0,0))
        win = font.render('Императора гордиться тобой, тебе полагается миска риса и фелинид-жена', True,(255,215,0))
        lose = font.render('Императора не доволен тобой, ты идёшь работать на урановый шахты через два дня', True, (255,215,0))
        harow = font.render('social credit:{}'.format(point), True,(255,215,0))
        lox = font.render('недавольсво императора:{}'.format(miss), True,(255,215,0))
        patrons = font.render('использовано патрон:{} из 6'.format(kolvo), True, (255,215,0))
        window.blit(lox, (10,20))
        window.blit(harow, (10,50))
        window.blit(patrons, (10,80))
        keys = key.get_pressed()  
        pyli.draw(window)
        pyli.update() 
        hero.reset()
        hero.update()
        clock.tick(FPS)
        mrasi.draw(window)
        mrasi.update()
        collides = sprite.groupcollide(pyli,mrasi, True,True)
        for  i in collides:
            point += 1
            kolvo -= 1
            mrasi.add(gnids(randint(2,3), 'pngaaa.com-671148.png', randint(90,610),0))
        if sprite.spritecollide(hero, mrasi, False) or miss >= 5:
            finish = True
            window.blit(lose, (50,200))
            mixer.music.stop()
            loser.play()
        if point >= 10:
            finish = True
            window.blit(win,(50, 200))
            mixer.music.stop()
            winner.play()
        display.update()
        