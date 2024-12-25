import pygame
import random
Blue=pygame.Color("blue")
yellow=pygame.Color("yellow")
crimison=pygame.Color("green")


pygame.init()
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super(). __init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit = False
        if self.rect.left<=0 or self.rect.right >= 500:
            self.velocity[0]=-self.velocity[0]
            boundery_hit=True
        if self.rect.top<=0 or self.rect.bottom >= 400:
            self.velocity[1]=-self.velocity[1]
            boundery_hit=True
def change_bgcolor():
    global bgcolor
    bgcolor = random.choice([blue,yellow,crimison])
all_sprites=pygame.sprite.Group()

blue=pygame.Color("blue")
sp1 = Sprite(blue,40,50)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,380)
all_sprites.add(sp1)
screen=pygame.display.set_mode((500,500))
done = False

while  not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
