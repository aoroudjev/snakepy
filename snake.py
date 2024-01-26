from collections import deque


class Snake:
    def __init__(self, start_position: tuple):
        self.snake_list = deque([start_position])  # position format: (x, y)
        self.direction = ''
        self.speed = 1

    def __len__(self):
        return len(self.snake_list)

    def check_collision_with_self(self):
        head = self.snake_list[-1]
        return head in list(self.snake_list)[:-1]

    def update(self, fruit_coords):
        head_x, head_y = self.snake_list[-1]
        if self.direction == "down":
            new_head = (head_x, head_y + self.speed)
        elif self.direction == "up":
            new_head = (head_x, head_y - self.speed)
        elif self.direction == "left":
            new_head = (head_x - self.speed, head_y)
        elif self.direction == "right":
            new_head = (head_x + self.speed, head_y)
        else:
            return

        self.snake_list.append(new_head)
        if new_head != fruit_coords:
            self.snake_list.popleft()

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction
