# Курсовой проект - Игра Змейка
## Описание

В ходе выполнения курсового проекта, было принято создать всем знакомую с детства игру - "Змейка". Код игры был нгаписан при помощи PyGame (pygame==2.3.0). 

PyGame - это набор модулей языка программирования Python, предназначенный для написания компьютерных игр и мультимедиа-приложений.

![screen](https://github.com/SergeiGlavinski/DZ/blob/main/%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9.png)

## Написание кода

В первую очередь были импортированы библиотека pygame и random.
```python
import pygame
from random import randrange
```

Первым действие при написание кода, было создано игровое поле, заданы его размеры, а так же размеры одной игровой клетки. 
```python
RES = 800
SIZE = 50
```

Начальное положение Змейки и еды для неё, генерируются рандомно.
```python
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE) # Начальное положение змейки
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE) #начальное положение яблока
```

Следующим действием были назначины клавиши управления. 
```python
klaviwa = {'W': True, 'S': True, 'A': True, 'D': True}
```

Без доработак управления не обошлось. Без дополнительных строк кода, у змейки была возможность разворачится в движении на 180 градусов, что противоречит правилам игры. Поэтому, для каждой клавиши был прописан блок if, который убирает этот недочёт.
```python
key = pygame.key.get_pressed()
    if key[pygame.K_w] and klaviwa['W']:
        dx, dy = 0, -1
        klaviwa = {'W': True, 'S': False, 'A': True, 'D': True}
```

В цикле while прописаны условия проигрыша. Если Змейка поедает сама себя или касается предолов игрового поля, игра засчитывает поражение, появляется надпись "Game Over" и игра заканчивается.
```python
 if x < 0 or x > RES or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
```
