import cv2
import math
import pygame

while True:
    max_width = 900
    max_height = 700

    while True:
        try:
            path = input("path: ")
            im = cv2.imread(path)  # read image
            break
        except:
            pass

    fontSize = 5
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # make it grayscale

    density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.      "
    length = len(density)

    result = input("Enter type text/screen: ")
    while result != "text" and result != "screen":
        result = input("Enter type text/screen: ")

    if result == "text":
        text = ""
        idx = 0
        for i in range(len(im)):
            for j in range(len(im[0])):
                OldRange = (255 - 0)
                NewRange = (0 - length)
                index = math.floor((((im[i][j] - 0) * NewRange) / OldRange) + 0)
                if index == length:
                    index -= 1
                text += density[index] + " "

            text += "\n"

        with open('img.txt', 'w') as f:
            f.write(text)


    elif result == "screen":
        pygame.init()
        screen = pygame.display.set_mode((fontSize * len(im), fontSize * len(im[0])))
        run = True

        font = pygame.font.Font('CourierPrime-Regular.ttf', 16)

        while run:

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            # draw
            screen.fill((0, 0, 0))  # background black
            for i in range(len(im)):
                for j in range(len(im[0])):
                    OldRange = (255 - 0)
                    NewRange = (0 - length)
                    index = math.floor((((im[i][j] - 0) * NewRange) / OldRange) + 0)
                    if index == length:
                        index -= 1

                    text = font.render(density[index], True, (255, 255, 255), (0, 0, 0))
                    rect = text.get_rect(topleft=(fontSize * j, fontSize * i))
                    screen.blit(text, rect)

                    # draw text

            pygame.display.flip()

        pygame.display.quit()
    s = input("[enter=go on else=exit]:")
    if s != "":
        break
