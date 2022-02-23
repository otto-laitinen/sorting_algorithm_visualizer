import pygame

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
