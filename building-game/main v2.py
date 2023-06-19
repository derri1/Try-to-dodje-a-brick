from pygame import *

#Основ. окно игры
win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Try to dodge a brick')
background = transform.scale(image.load('background.png'), (win_width, win_height))

#Константы
run = True
finish = False
clock = time.Clock()
life = 3
score = 0

#Класс про-родитель
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  player_speed, size_x, size_y,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 160))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#Класс игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700:
            self.rect.x += self.speed

#Сам игрок
player = Player('player.png', 360, 340, 3, 80, 150)

#Текст
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
lose = font2.render('Get the L', True, (180, 0, 0))

#Цикл игры
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        #Очки
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        
        window.blit(background,(0,0))
        player.update()
        player.reset()
    display.update()