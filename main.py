from typing import Tuple, List

import pygame
from pygame.locals import *
from snake import Snake

WINDOW_SIZE = (300, 300)
GRID_SQUARE_SIZE = 20


def draw_grid(snake_list: List[Tuple]):
    for x in range(0, WINDOW_SIZE[0], GRID_SQUARE_SIZE):
        for y in range(0, WINDOW_SIZE[1], GRID_SQUARE_SIZE):
            rect = pygame.Rect(x, y, GRID_SQUARE_SIZE, GRID_SQUARE_SIZE)
            if (y, x) in snake_list:
                pygame.draw.rect(screen, "red", rect, 2)
            else:
                pygame.draw.rect(screen, "white", rect, 1)


def main():
    # Initialize screen
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('SnakePy')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('black')

    clock = pygame.time.Clock()
    pygame.display.update()

    snake = Snake((0, 0))

    # Event loop
    while True:

        clock.tick(1)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            # elif event.type == KEYDOWN:
            #     if event.key == K_UP:
            #         snake.direction = 'up'
            #     if event.key == K_DOWN:
            #         snake.direction = 'down'
            #     if event.key == K_LEFT:
            #         snake.direction = 'left'
            #     if event.key == K_RIGHT:
            #         snake.direction = 'right'

        print(snake.snake_list)
        draw_grid(snake.snake_list)
        pygame.display.update()
        snake.update()


if __name__ == '__main__':
    main()
