class Snake:
    def __init__(self, position: tuple):
        self.snake_list = [position]  # position format: (x, y)
        self.direction = "down"

    def __len__(self):
        return len(self.snake_list)

    def update(self):
        head_x, head_y = self.snake_list[-1]
        if self.direction == "down":
            self.snake_list.append((head_x, head_y + 1))
            self.snake_list.pop(0)
        if self.direction == "up":
            self.snake_list.append((head_x, head_y - 1))
            self.snake_list.pop(0)
        if self.direction == "left":
            self.snake_list.append((head_x - 1, head_y))
            self.snake_list.pop(0)
        if self.direction == "right":
            self.snake_list.append((head_x + 1, head_y))
            self.snake_list.pop(0)

    def grow(self):
        pass

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction
