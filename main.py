from time import sleep

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 20


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

    def create_dialog_box(msg):
        mbx = 0
        mby = 335
        mb2x = 5
        mb2y = 340
        mb = pygame.Rect((500, 165))
        mb2 = pygame.Rect((490, 152))
        pygame.draw.rect(win, (255, 255, 255), mb)
        pygame.draw.rect(win, (0, 0, 0), mb2)
#      mb = pygame.Rect(win, (255, 255, 255), (mbx, mby, 500, 165))\
#      mb2 = pygame.Rect(win, (0, 0, 0), (mb2x, mb2y, 490, 152))
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(msg, False, (255, 255, 255))
        win.blit(text, (20, 350))
        pygame.display.update()
        if keys[pygame.K_RETURN]:
            mb.inflate_ip(0.00, 0.00)
            print("mb moved")
            mb2.inflate_ip(0.00, 0.00)
            print("mb2 moved")
            pygame.display.update()
            print("updated")



    create_dialog_box("hello my friend!")

pygame.quit()