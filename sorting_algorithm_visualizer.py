from ctypes import create_string_buffer
import pygame
import random

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    SIDE_PADDING = 100
    TOP_PADDING = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = round(
            (self.height - self.TOP_PADDING) / (self.max_value - self.min_value)
        )
        # starting point of blocks on the x-axis:
        self.start_x = self.SIDE_PADDING // 2


def generate_initial_list(n, min_value, max_value):
    lst = []

    for _ in range(n):
        value = random.randint(min_value, max_value)
        lst.append(value)

    return lst


# Pygame event loop
def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_value = 0
    max_value = 100

    # Generate initial list
    lst = generate_initial_list(n, min_value, max_value)

    # Draw the window
    draw_info = DrawInformation(700, 700, lst)

    while run:
        clock.tick(60)  # 60 fps

        pygame.display.update()

        # Returns a list of occurred events since the last loop
        for event in pygame.event.get():
            # If the user click on the red x on the top right of window
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
