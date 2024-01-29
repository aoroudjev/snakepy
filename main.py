import pygame
import random
from pygame.locals import *
from snake import Snake

WINDOW_SIZE = (500, 500)
GRID_SQUARE_SIZE = 20


def set_fruit_coords(snake: Snake) -> tuple:
    grid = [(i, j) for i in range(WINDOW_SIZE[0] // GRID_SQUARE_SIZE)
            for j in range(WINDOW_SIZE[1] // GRID_SQUARE_SIZE)]
    empty_coords = [coord for coord in grid if coord not in snake.snake_list]
    fruit = random.choice(empty_coords)
    return fruit


def draw_fruit(screen: pygame.display, coords: tuple):
    coord_x, coord_y = coords
    fruit = pygame.Rect(coord_x * GRID_SQUARE_SIZE,
                        coord_y * GRID_SQUARE_SIZE,
                        GRID_SQUARE_SIZE,
                        GRID_SQUARE_SIZE)
    pygame.draw.rect(screen, "green", fruit)


def draw_snake(screen: pygame.display, snake: Snake) -> None:
    for snake_x, snake_y in snake.snake_list:
        snake_seg = pygame.Rect(snake_x * GRID_SQUARE_SIZE,
                                snake_y * GRID_SQUARE_SIZE,
                                GRID_SQUARE_SIZE,
                                GRID_SQUARE_SIZE)
        pygame.draw.rect(screen, "red", snake_seg)


def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('SnakePy')
    font = pygame.font.SysFont("Roboto", 24)
    img = font.render('hello', True, (255, 255, 255))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('black')

    clock = pygame.time.Clock()
    pygame.display.update()

    snake = Snake(tuple(int((x//GRID_SQUARE_SIZE)/2) for x in WINDOW_SIZE))
    fruit = set_fruit_coords(snake)

    movement_made = False
    game_over = False
    # Event loop

    while True:
        clock.tick(10)
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

        draw_snake(screen, snake)
        draw_fruit(screen, fruit)
        pygame.display.update()

        snake.update(fruit)
        if snake.snake_list[-1] == fruit:
            fruit = set_fruit_coords(snake)

        head_x, head_y = snake.snake_list[-1]
        if (head_x < 0 or head_y < 0 or
                head_x >= WINDOW_SIZE[0] // GRID_SQUARE_SIZE or
                head_y >= WINDOW_SIZE[1] // GRID_SQUARE_SIZE or
                snake.check_collision_with_self()):
            game_over = True

        if game_over:
            game_over_message = font.render('Game Over', True, (255, 255, 0))
            screen.blit(game_over_message, tuple((x/2 for x in WINDOW_SIZE)))
            pygame.display.update()
            pygame.time.wait(2000)
            return

        movement_made = False
        screen.fill('black')


if __name__ == '__main__':
    main()
