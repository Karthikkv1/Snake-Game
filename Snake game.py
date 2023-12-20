# program to Develop our First Game Using pygame module of python

import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Defining colours for line 25
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating game Window
screen_width = 1200
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# To add background image to game
background_image = pygame.image.load("Background.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)).convert_alpha()

# To add image to Starting screen of game
starting_image = pygame.image.load("GameStart.png")
starting_image = pygame.transform.scale(starting_image, (screen_width, screen_height)).convert_alpha()

# To add image to Game over screen of game
gameOver_image = pygame.image.load("GameOver.png")
gameOver_image = pygame.transform.scale(gameOver_image, (screen_width, screen_height)).convert_alpha()


# Creating title for our game
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


def plot_snake(gameWindow, color, snk_list, side1, side2):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, side1, side2])


def welcome():
    pygame.mixer.music.load('Coding 4 (For event videos).mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 210, 229))  # colour RGB Values
        gameWindow.blit(starting_image, (0, 0))
        text_screen("WELCOME TO SNAKE GAME", red, 300, 250)
        text_screen("Press Space bar to play", red, 320, 300)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Coding 3(For event videos).mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Creating a game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    sideX = 45
    sideY = 55
    side1 = 30
    side2 = 30
    fps = 25

    velocityX = 0
    velocityY = 0
    snk_list = []
    snk_length = 1
    # Check if HighScore file exists
    if (not os.path.exists("HighScore.txt")):
        with open("HighScore.txt", "w") as f:
            f.write("0")

    with open("HighScore.txt", "r") as f:
        hiscore = f.read()

    foodX = random.randint(20, screen_width / 2)
    foodY = random.randint(20, screen_height / 2)

    score = 0
    init_velocity = 5

    while not exit_game:
        if game_over:
            with open("HighScore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(gameOver_image, (0, 0))
            text_screen("GAME OVER! Press Enter to  Play Again", red, 190, 300)
            text_screen("Your Score:" + str(score), red, 400, 350)

            text_screen("Game By KARTHIK K V", red, 500, 500)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityX = init_velocity  # plus
                        velocityY = 0

                    if event.key == pygame.K_LEFT:
                        velocityX = - init_velocity  # minus
                        velocityY = 0

                    if event.key == pygame.K_UP:
                        velocityY = - init_velocity  # minus
                        velocityX = 0

                    if event.key == pygame.K_DOWN:
                        velocityY = init_velocity  # plus
                        velocityX = 0

                    if event.key == pygame.K_q:
                        score = score + 50

            sideX = sideX + velocityX
            sideY = sideY + velocityY

            if abs(sideX - foodX) < 6 and abs(sideY - foodY) < 6:
                score = score + 10
                foodX = random.randint(20, screen_width / 2)
                foodY = random.randint(20, screen_height / 2)
                snk_length = snk_length + 5  # or snk_length +=5
                if score > int(hiscore):
                    hiscore = score

            # Creating ground for our game with white colour
            gameWindow.fill(white)
            gameWindow.blit(background_image, (0, 0))
            text_screen("Score:" + str(score) + "  HighScore:" + str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [foodX, foodY, side1, side2])

            head = []
            head.append(sideX)
            head.append(sideY)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Coding 1(For event videos).mp3')
                pygame.mixer.music.play()

            if sideX < 0 or sideX > screen_width or sideY < 0 or sideY > screen_height:
                game_over = True
                # print("GAME OVER")
                pygame.mixer.music.load('Coding 1(For event videos).mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, side1, side2)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()