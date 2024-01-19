class Snake:
    def __init__(self, start_position: tuple):
        self.snake_list = [start_position]  # position format: (x, y)
        self.direction = ""
        self.speed = 1

    def __len__(self):
        return len(self.snake_list)

    def update(self):
        head_x, head_y = self.snake_list[-1]
        if self.direction == "down":
            self.snake_list.append((head_x, head_y + self.speed))
        elif self.direction == "up":
            self.snake_list.append((head_x, head_y - self.speed))
        elif self.direction == "left":
            self.snake_list.append((head_x - self.speed, head_y))
        elif self.direction == "right":
            self.snake_list.append((head_x + self.speed, head_y))
        else:
            return
        self.snake_list.pop(0)

    def grow(self):
        pass

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction
