import pygame
from draw_list import draw_list


def draw(draw_info, algorithm_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # Draw algorithm name
    title = draw_info.LARGE_FONT.render(
        f"{'Ascending' if ascending else 'Descending'} {algorithm_name}",
        1,
        draw_info.GREEN,
    )
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    # Draw controls on the screen
    controls = draw_info.FONT.render(
        "R - Reset, | SPACE - Start Sorting | A - Ascending | D - Descending",
        1,
        draw_info.BLACK,
    )
    # Center
    draw_info.window.blit(
        controls, (draw_info.width / 2 - controls.get_width() / 2, 40)
    )

    # Draw sorting options
    sorting = draw_info.FONT.render(
        "B - Bubble Sort | I - Insertion Sort", 1, draw_info.BLACK
    )
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 65))

    draw_list(draw_info)
    pygame.display.update()
