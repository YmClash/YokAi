import pygame
import random

pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

COLOR = [random.randint(0, 255), random.randint(0, 250), random.randint(0, 255)]
COLOR_2 = [random.randint(0, 255), random.randint(0, 250), random.randint(0, 255)]
COLOR_3 = [random.randint(0, 255), random.randint(0, 250), random.randint(0, 255)]
COLOR_4 = [random.randint(0, 255), random.randint(0, 250), random.randint(0, 255)]

HAUTEUR = 300
LARGEUR = 300
FPS = 60

screen = pygame.display.set_mode((HAUTEUR, LARGEUR))
clock = pygame.time.Clock()

# object  player

circle = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
carre = pygame.Rect(random.randint(1,300),random.randint(1,300) , 50, 50)
carre_2 = pygame.Rect(random.randint(1,300),random.randint(1,300) , random.randint(20,100), random.randint(20,100))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            carre.y -= 2
            # carre_2 -= 2
        if event.key == pygame.K_DOWN:
            carre.y += 2
        if event.key == pygame.K_LEFT:
            carre.x -= 2
        if event.key == pygame.K_RIGHT:
            carre.x += 2


    screen.fill(COLOR)

    pygame.draw.circle(screen, COLOR_2, circle, radius=20)
    pygame.draw.rect(screen, COLOR_3, carre)
    pygame.draw.ellipse(screen,COLOR_4,carre_2)


    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
