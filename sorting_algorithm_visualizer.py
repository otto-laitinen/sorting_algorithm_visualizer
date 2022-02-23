import pygame
import random
import math

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

    FONT = pygame.font.SysFont("comicsans", 15)
    LARGE_FONT = pygame.font.SysFont("comicsans", 20)
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
        self.block_height = math.floor(
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

    # Draw controls on the screen
    controls = draw_info.FONT.render(
        "R - Reset, | SPACE - Start Sorting | A - Ascending | D - Descending",
        1,
        draw_info.BLACK,
    )
    # Center
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 5))

    # Draw sorting options
    sorting = draw_info.FONT.render(
        "B - Bubble Sort | I - Insertion Sort", 1, draw_info.BLACK
    )
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 35))

    draw_list(draw_info)
    pygame.display.update()


# Draw individual blocks
def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_block = (
            draw_info.SIDE_PADDING // 2,
            draw_info.TOP_PADDING,
            draw_info.width - draw_info.SIDE_PADDING,
            draw_info.height - draw_info.TOP_PADDING,
        )

        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_block)

    for index, value in enumerate(lst):
        x = draw_info.start_x + index * draw_info.block_width
        y = draw_info.height - (value - draw_info.min_value) * draw_info.block_height

        # The order of colors for the blocks is: dark grey, grey, light grey
        color = draw_info.SHADES_OF_GREY[index % 3]

        if index in color_positions:
            color = color_positions[index]

        pygame.draw.rect(
            draw_info.window, color, (x, y, draw_info.block_width, draw_info.height)
        )

    if clear_bg:
        pygame.display.update()


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

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

    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)  # 60 fps

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        # Returns a list of occurred events since the last loop
        for event in pygame.event.get():
            # If the user click on the red x on the top right of window
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            # R --> generate a new random list
            if event.key == pygame.K_r:
                lst = generate_initial_list(n, min_value, max_value)
                draw_info.set_list(lst)
                sorting = False

            # Space --> start sorting
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)

            # A --> Ascending order
            elif event.key == pygame.K_a and sorting == False:
                ascending = True

            # D --> Descending order
            elif event.key == pygame.K_d and sorting == False:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()
