import pygame
import random

pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("Untitled.png")

# Title and icon (icons should be 32x32, sprites should be 64x64)
pygame.display.set_caption("Steven Shooter")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player (64x64)
MainCharacter = pygame.image.load("maincharacter.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
Enemy = pygame.image.load("ErickSmaller.png")
EnemyX = random.randint(50, 650)
EnemyY = random.randint(0, 215)
EnemyX_change = 2
EnemyY_change = 40

# Dildo
Bullet = pygame.image.load("52414-01.png")
BulletX = playerX
BulletY = playerY
BulletX_change = 0
BulletY_change = 10
BulletState = "ready"


def player(x, y):
    screen.blit(MainCharacter, (x, y))


def enemy(x, y):
    screen.blit(Enemy, (x, y))


def fire_bullet(x, y):
    global BulletState
    BulletState = "fire"
    screen.blit(Bullet, (x - 17, y - 30))


# keeping the window open and giving it the ability to close
running = True
while running:
    # this is to color screen. notice how .fill is connected to'screen'
    # which is a variable not an actual component of pygame.
    screen.fill((240, 240, 69))
    # background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                playerX_change = 6
            if event.key == pygame.K_UP:
                playerY_change = -6
            if event.key == pygame.K_DOWN:
                playerY_change = 6
            if event.key == pygame.K_SPACE:
                fire_bullet(BulletX, BulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    # Player Coordinate += Player velocity
    playerX += playerX_change
    playerY += playerY_change
    # Player Boundary
    if playerX <= -6:
        playerX = -6
    elif playerX >= 741:
        playerX = 741
    if playerY <= 0:
        playerY = 0
    elif playerY >= 520:
        playerY = 520

    # Enemy Coordinate += Enemy velocity
    EnemyX += EnemyX_change
    # Enemy Boundary
    if EnemyX <= -6:
        EnemyX_change = 2
        EnemyY += EnemyY_change
    elif EnemyX >= 703:
        EnemyX_change = -2
        EnemyY += EnemyY_change
    if EnemyY <= 0:
        EnemyY = 0
    elif EnemyY >= 520:
        EnemyY = 520
    player(playerX, playerY)
    enemy(EnemyX, EnemyY)

    # Bullet Movement
    if BulletState == "ready":
        BulletY = playerY
        BulletX = playerX
    elif BulletState == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change
    if BulletY <= 0:
        BulletState = "ready"
    pygame.display.update()