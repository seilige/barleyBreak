import pygame
import random

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True
fps = 60
font = pygame.font.Font(None, 72)
k = 0
rect = [0,0]
mainCords = [300, 300]
randomLst = []
mainLst = [[dict(), dict()] for i in range(4)]

while len(randomLst) != 15:
    num = random.randint(1, 15)
    if(num not in randomLst):
        randomLst.append(num)

randomLst.append(16)

for i in range(4):
    for x in range(4):
        if(k == 15):
            text = font.render(" ", True, (32, 230, 141))
        else:
            text = font.render(f"{randomLst[k]}", True, (32, 230, 141))

        mainLst[i][1][f"{randomLst[k]}"] = [text, tuple(rect)]
        mainLst[i][0][f"{randomLst[k]}"] = pygame.Rect(rect[0], rect[1], 100, 100)
        rect[0] += 100        
        k += 1

    rect[1] += 100
    rect[0] = 0

while run:
    value = -1
    mainX = 0
    mainY = 0

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False

        if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
            x, y = pygame.mouse.get_pos()

            for i in mainLst:
                for l in i[0].keys():
                    if(x in [b for b in range(i[0][l].x, i[0][l].x+101)] and y in [b for b in range(i[0][l].y, i[0][l].y+101)]):
                        xx = i[0][l].x
                        yy = i[0][l].y

                        if(
                            xx - 100 == mainCords[0] and yy == mainCords[1] or \
                            xx + 100 == mainCords[0] and yy == mainCords[1] or \
                            xx == mainCords[0] and yy - 100 == mainCords[1] or \
                            xx == mainCords[0] and yy + 100 == mainCords[1]
                        ):
                            mainX = mainCords[0]
                            mainY = mainCords[1]
                            i[0][l].x = mainCords[0]
                            i[0][l].y = mainCords[1]
                            mainCords[0] = xx
                            mainCords[1] = yy
                            value = l

    for i in mainLst:
        for x in i[0].keys():
            if(x == "16"):
                i[0][x].x = mainCords[0]
                i[0][x].y = mainCords[1]

                pygame.draw.rect(screen, (98, 32, 230), i[0][x])
            else:
                pygame.draw.rect(screen, (255,255,255), i[0][x])


        for x in i[1].keys():
            if(value != -1):
                for l in range(len(mainLst)):
                    for g in mainLst[l][1].keys():
                        if(g == value):
                            mainLst[l][1][g][1] = list(mainLst[l][1][g][1])
                            mainLst[l][1][g][1][0] = mainX
                            mainLst[l][1][g][1] = tuple(mainLst[l][1][g][1])

                            mainLst[l][1][g][1] = list(mainLst[l][1][g][1])
                            mainLst[l][1][g][1][1] = mainY
                            mainLst[l][1][g][1] = tuple(mainLst[l][1][g][1])

            screen.blit(i[1][x][0], i[1][x][1])

    clock.tick(fps)
    pygame.time.delay(10)
    pygame.display.update()
