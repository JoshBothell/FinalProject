# Josh Bothell
# PyGame Template
import pygame
import random
import math

WIDTH = 1024
HEIGHT = 768
FPS = 30
SPEED = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TANX!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = player_tank
        # self.image_orig.fill(BLUE)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.last_update = pygame.time.get_ticks()
        self.rot = 0
        self.rot_speed = None
        self.position = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rotate("LEFT")
        if keystate[pygame.K_RIGHT]:
            self.rotate("RIGHT")
        if keystate[pygame.K_UP]:
            self.drive()

    def rotate(self, direction):
        now = pygame.time.get_ticks()
        if direction == "RIGHT":
            self.rot_speed = -7
        if direction == "LEFT":
            self.rot_speed = 7
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            print(self.rect.center)

    def drive(self):
        dx = math.cos(math.radians(self.rot))
        dy = math.sin(math.radians(self.rot))
        self.position = (self.position[0] + dx * SPEED, self.position[1] - dy * SPEED)


# load sprites
player_tank = pygame.image.load("img/tank_red.png")


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # all_sprites.update()
    screen.fill(BLACK)
    # all_sprites.draw(screen)
    screen.blit(player.image, player.position)
    print(player.position)
    player.update()
    pygame.display.update()
    pygame.display.flip()

pygame.quit()
