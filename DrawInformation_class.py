import pygame
import math

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 200, 0
    RED = 200, 0, 0
    GREY = 128, 128, 128
    LIGHT_GREY = 160, 160, 160
    DARK_GREY = 192, 192, 192
    BACKGROUND_COLOR = WHITE

    SHADES_OF_GREY = [GREY, LIGHT_GREY, DARK_GREY]

    FONT = pygame.font.SysFont("arial", 15)
    LARGE_FONT = pygame.font.SysFont("arial", 20)
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
