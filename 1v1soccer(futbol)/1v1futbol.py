import pygame,random
genislik = 1400
yukseklik = 800

pygame.init()

goruntu_yuzeyi = pygame.display.set_mode((genislik,yukseklik))
t1 = 0
t2 = 0
tx = random.choice([-1,1])
ty = random.choice([-1,1])
t_hız = 1
takım2_puan = 0
takım1_puan = 0
durum = True
font = pygame.font.Font("AttackGraffiti.ttf", 24)
takım1_skor = font.render('TAKIM 1 SKOR:' + str(takım1_puan),True,(0,0,0))
takım1_skor_koordinat = takım1_skor.get_rect()
takım1_skor_koordinat.y = 50
takım1_skor_koordinat.x = 50
takım2_skor = font.render('TAKIM 2 SKOR:' + str(takım2_puan),True,(0,0,0))
takım2_skor_koordinat = takım2_skor.get_rect()
takım2_skor_koordinat.y = 50
takım2_skor_koordinat.x = genislik - 200

class Takım_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('football-player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.bottom = yukseklik // 2
    def update(self):
        self.move()
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.rect.left>0:
            self.rect.x -= 1

        elif keys[pygame.K_d] and self.rect.right<genislik:
            self.rect.x += 1

        elif keys[pygame.K_w] and self.rect.top >= 0:
            self.rect.y -= 1
        elif keys[pygame.K_s] and self.rect.bottom <= yukseklik:
            self.rect.y += 1
    def reset_positions(self):
        self.rect.bottom = yukseklik // 2
        self.rect.centerx = 200
        pygame.time.delay(2000)  # Use pygame.time.delay to pause the game for 2000 milliseconds (2 seconds)

class Takım_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../../Downloads/soccer-player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = genislik - 200
        self.rect.bottom = yukseklik // 2
    def update(self):
        self.move()
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left>0:
            self.rect.x -= 1

        elif keys[pygame.K_RIGHT] and self.rect.right<genislik:
            self.rect.x += 1

        elif keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.y -= 1
        elif keys[pygame.K_DOWN] and self.rect.bottom <= yukseklik:
            self.rect.y += 1

    def reset_positions(self):
        self.rect.bottom = yukseklik // 2
        self.rect.centerx = genislik - 200
        pygame.time.delay(2000)  # Use pygame.time.delay to pause the game for 2000 milliseconds (2 seconds)


class Kale_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../../Downloads/goal2.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        self.rect.bottom = yukseklik // 2


class Kale_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../../../Downloads/goal.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = genislik - 50
        self.rect.bottom = yukseklik // 2

class Top(pygame.sprite.Sprite):
    def __init__(self,takım1,takım2,takım1_puan,takım2_puan,kale_1,kale_2,futbol_topu):
        global rect,image
        super().__init__()
        self.image = pygame.image.load('top.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = genislik // 2
        self.rect.bottom = yukseklik // 2
        self.takım1 = takım1
        self.takım2 = takım2
        self.takım1_puan = takım1_puan
        self.takım2_puan = takım2_puan
        self.kale_1 = kale_1
        self.kale_2 = kale_2
        self.futbol_topu = futbol_topu

    def update(self):
        global ty, tx, t_hız

        self.rect.x = self.rect.x + (t_hız * tx)
        self.rect.y = self.rect.y + (t_hız * ty)

        if self.rect.left <= 0 or self.rect.right >= genislik:
            tx = -1 * tx
        if self.rect.top <= 0 or self.rect.bottom >= yukseklik:
            ty = -1 * ty

        if self.rect.left > genislik or self.rect.right < 0 or self.rect.top > yukseklik or self.rect.bottom < 0:
            self.reset_positions()

        if pygame.sprite.groupcollide(kale_1, futbol_topu, False, False):
            self.reset_positions()
            self.takım2_puan += 1
            print('TAKIM 1:', str(self.takım1_puan), 'TAKIM 2:', str(self.takım2_puan))

        if pygame.sprite.groupcollide(kale_2, futbol_topu, False, False):
            self.reset_positions()
            self.takım1_puan += 1
            print('TAKIM 1:', str(self.takım1_puan), 'TAKIM 2:', str(self.takım2_puan))

        if pygame.sprite.groupcollide(self.takım1, futbol_topu, False, False):
            ty = -1 * ty
            tx = -1 * tx

        if pygame.sprite.groupcollide(self.takım2, futbol_topu, False, False):
            ty = -1 * ty
            tx = -1 * tx

    def reset_positions(self):
        for player in self.takım1:
            player.reset_positions()

        for player in self.takım2:
            player.reset_positions()

        self.rect.bottom = yukseklik // 2
        self.rect.centerx = genislik // 2
        pygame.time.delay(2000)  # Use pygame.time.delay to pause the game for 2000 milliseconds (2 seconds)




kale_1 = pygame.sprite.Group()
kale1 = Kale_1()
kale_1.add(kale1)
kale_2 = pygame.sprite.Group()
kale2 = Kale_2()
kale_2.add(kale2)
takım1 = pygame.sprite.Group()
takım_1 = Takım_1()
takım1.add(takım_1)
takım2 = pygame.sprite.Group()
takım_2 = Takım_2()
takım2.add(takım_2)
futbol_topu = pygame.sprite.Group()
top = Top(takım1,takım2,takım1_puan,takım2_puan,kale_1,kale_2,futbol_topu)
futbol_topu.add(top)

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False

    goruntu_yuzeyi.fill((0, 153, 76))
    pygame.draw.line(goruntu_yuzeyi, (255, 255, 255), (100, 0), (100, yukseklik), 5)
    pygame.draw.line(goruntu_yuzeyi, (255, 255, 255), (genislik - 100, 0), (genislik - 100, yukseklik), 5)
    pygame.draw.circle(goruntu_yuzeyi, (255, 255, 255), (genislik // 2, yukseklik // 2), 100, 5)
    pygame.draw.line(goruntu_yuzeyi, (255, 255, 255), (genislik // 2, 0), (genislik // 2, yukseklik), 5)

    takım1_puan = top.takım1_puan
    takım2_puan = top.takım2_puan

    current_takım1_skor_text = 'TAKIM 1 SKOR:' + str(takım1_puan)
    current_takım2_skor_text = 'TAKIM 2 SKOR:' + str(takım2_puan)

    if takım1_skor != font.render(current_takım1_skor_text, True, (0, 0, 0)) or takım2_skor != font.render(current_takım2_skor_text, True, (0, 0, 0)):
        takım1_skor = font.render(current_takım1_skor_text, True, (0, 0, 0))
        takım2_skor = font.render(current_takım2_skor_text, True, (0, 0, 0))

    goruntu_yuzeyi.blit(takım1_skor, takım1_skor_koordinat)
    goruntu_yuzeyi.blit(takım2_skor, takım2_skor_koordinat)


    futbol_topu.update()
    futbol_topu.draw(goruntu_yuzeyi)
    kale_1.update()
    kale_1.draw(goruntu_yuzeyi)
    kale_2.update()
    kale_2.draw(goruntu_yuzeyi)
    takım1.update()
    takım1.draw(goruntu_yuzeyi)
    takım2.update()
    takım2.draw(goruntu_yuzeyi)

    pygame.display.update()

pygame.quit()

pygame.quit()

