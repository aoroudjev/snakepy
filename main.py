import pygame
from pygame.locals import *
from snake import Snake

WINDOW_SIZE = (500, 500)
GRID_SQUARE_SIZE = 20


def draw_grid() -> None:
    for x in range(0, WINDOW_SIZE[0] // GRID_SQUARE_SIZE):
        for y in range(0, WINDOW_SIZE[1] // GRID_SQUARE_SIZE):
            rect = pygame.Rect(x * GRID_SQUARE_SIZE,
                               y * GRID_SQUARE_SIZE,
                               GRID_SQUARE_SIZE,
                               GRID_SQUARE_SIZE)
            pygame.draw.rect(screen, "white", rect, 1)


def draw_snake(snake: Snake) -> None:
    for snake_x, snake_y in snake.snake_list:
        snake_seg = pygame.Rect(snake_x * GRID_SQUARE_SIZE,
                                snake_y * GRID_SQUARE_SIZE,
                                GRID_SQUARE_SIZE,
                                GRID_SQUARE_SIZE)
        pygame.draw.rect(screen, "red", snake_seg)


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

    snake = Snake(tuple(int((elem // GRID_SQUARE_SIZE) / 2) for elem in WINDOW_SIZE))
    last_time = pygame.time.get_ticks()
    movement_made = False

    # Event loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and not movement_made:
                movement_made = True
                if event.key == K_UP and snake.direction != 'down':
                    snake.set_direction('up')
                elif event.key == K_DOWN and snake.direction != 'up':
                    snake.set_direction('down')
                elif event.key == K_LEFT and snake.direction != 'right':
                    snake.set_direction('left')
                elif event.key == K_RIGHT and snake.direction != 'left':
                    snake.set_direction('right')
                else:
                    movement_made = False

        print(f'head: {snake.snake_list}, direction: {snake.get_direction()}')

        # draw_grid()
        draw_snake(snake)
        pygame.display.update()

        current_time = pygame.time.get_ticks()
        if current_time - last_time > 100:
            snake.update()
            last_time = current_time
            movement_made = False

        screen.fill('black')


if __name__ == '__main__':
    main()
