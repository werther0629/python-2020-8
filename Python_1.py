import pygame

pygame.init()
win = pygame.display.set_mode((600,500))
pygame.display.set_caption("First gmae")
isjump = False
jumpCount = 10
x = 50
y = 400
width = 30
height = 40
vel = 10
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    if keys[pygame.K_a] and x > 0 :
        x -= vel
    if keys[pygame.K_d] and x < 600 - width:
        x += vel
    if not (isjump):
        if keys[pygame.K_w] :
            isjump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= neg * (jumpCount**2)* 0.5
            jumpCount -= 1
        else:
            isjump = False
            jumpCount = 10
            
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()


    
