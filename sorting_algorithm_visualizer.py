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
    LIGHT_GREY = 160, 160, 160
    DARK_GREY = 192, 192, 192
    BACKGROUND_COLOR = WHITE

    SHADES_OF_GREY = [GREY, LIGHT_GREY, DARK_GREY]

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


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()


# Draw individual blocks
def draw_list(draw_info):
    lst = draw_info.lst

    for index, value in enumerate(lst):
        x = draw_info.start_x + index * draw_info.block_width
        y = draw_info.height - (value - draw_info.min_value) * draw_info.block_height

        # The order of colors for the blocks is: grey, light grey, dark grey
        color = draw_info.SHADES_OF_GREY[index % 3]

        pygame.draw.rect(
            draw_info.window, color, (x, y, draw_info.block_width, draw_info.height)
        )


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

        draw(draw_info)

        # Returns a list of occurred events since the last loop
        for event in pygame.event.get():
            # If the user click on the red x on the top right of window
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            # If user presses R on keyboard, generate a new random list
            if event.key == pygame.K_r:
                lst = generate_initial_list(n, min_value, max_value)
                draw_info.set_list(lst)

    pygame.quit()


if __name__ == "__main__":
    main()
