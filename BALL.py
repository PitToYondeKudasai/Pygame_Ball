## Ball Game ##
import pygame
WIDTH = 500
HEIGHT = 500
GREEN = (150,255,150)
RED = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (100, 100))

rect = ball.get_rect()

speed = [2,4]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > WIDTH:
        speed[0] = - speed[0]
    if rect.top < 0 or rect.bottom > HEIGHT:
        speed[1] = - speed[1]
    screen.fill(GREEN)
    pygame.draw.rect(screen,GREEN, rect,1)
    screen.blit(ball, rect)
    pygame.display.update()
    
pygame.quit()
