import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Color Change Event")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

CHANGE_SPRITE_COLOR_EVENT = pygame.USEREVENT + 1

class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, size=50):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.original_color = color

    def change_color(self):
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)

    def update(self):
        pass

all_sprites = pygame.sprite.Group()

sprite1 = MySprite(RED, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
sprite2 = MySprite(BLUE, 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

all_sprites.add(sprite1, sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pygame.event.post(pygame.event.Event(CHANGE_SPRITE_COLOR_EVENT))
        
        if event.type == CHANGE_SPRITE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
