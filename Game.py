import pygame
from random import randrange


def game_snake():

    # Размеры окна и головы змейки
    RES = 800
    SIZE = 50

    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE) # Начальное положение змейки
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE) #начальное положение яблока
    klaviwa = {'W': True, 'S': True, 'A': True, 'D': True}
    dlina = 1 # Длина змеи
    snake = [(x, y)]
    dx, dy = 0,0 # Напривление движения
    speed = 5 # Скорость змейки
    score = 0

    pygame.init()
    screen = pygame.display.set_mode([RES, RES]) # Рабочее окно
    clock = pygame.time.Clock() #Регулирование скорости
    font_score = pygame.font.SysFont('Arial', 26, bold = True)
    font_end = pygame.font.SysFont('Arial', 66, bold = True)
    font_restart = pygame.font.SysFont('Arial', 36, bold = True)
    img = pygame.image.load('1.png').convert()


    while True:
        screen.blit(img, (0,0))
        # Вывод змейки и яблока на экран
        [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
        pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))
        # Надпись
        render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
        screen.blit(render_score, (5, 5))
        # Передвижение змейки
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-dlina:]
        # Поединае яблока
        if snake[-1] == apple:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            dlina += 1
            speed += 1
            score += 1
        # Game Over
        if x < 0 or x > RES or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
                screen.blit(render_end, (RES // 2 - 200, RES // 3))
                render_restart = font_restart.render('Press R to restart', 1, pygame.Color('orange'))
                screen.blit(render_restart, (RES // 2 - 150, RES // 2))
                render_restart = font_restart.render('Press Q to quit', 1, pygame.Color('orange'))
                screen.blit(render_restart, (RES // 2 - 140, 500))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            exit()
                        if event.key == pygame.K_r:
                            game_snake()



        pygame.display.flip()
        clock.tick(speed)

        # Упраление
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and klaviwa['W']:
            dx, dy = 0, -1
            klaviwa = {'W': True, 'S': False, 'A': True, 'D': True}

        if key[pygame.K_s] and klaviwa['S']:
            dx, dy = 0, 1
            klaviwa = {'W': False, 'S': True, 'A': True, 'D': True}

        if key[pygame.K_a] and klaviwa['A']:
            dx, dy = -1, 0
            klaviwa = {'W': True, 'S': True, 'A': True, 'D': False}

        if key[pygame.K_d] and klaviwa['D']:
            dx, dy = 1, 0
            klaviwa = {'W': True, 'S': True, 'A': False, 'D': True}

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


game_snake()