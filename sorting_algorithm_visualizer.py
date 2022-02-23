import pygame

from draw import draw
from DrawInformation_class import DrawInformation
from generate_list import generate_initial_list
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

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

    # Default algorithm
    algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    algorithm_generator = None

    while run:
        clock.tick(100)  # Speed of the algorithm

        if sorting:
            try:
                next(algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, algorithm_name, ascending)

        # Returns a list of occurred events since the last loop
        for event in pygame.event.get():
            # If the user click on the red x on the top right of window
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            # R --> generate a random list
            if event.key == pygame.K_r:
                lst = generate_initial_list(n, min_value, max_value)
                draw_info.set_list(lst)
                sorting = False

            # Space --> start sorting
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                algorithm_generator = algorithm(draw_info, ascending)

            # A --> Ascending order
            elif event.key == pygame.K_a and sorting == False:
                ascending = True

            # D --> Descending order
            elif event.key == pygame.K_d and sorting == False:
                ascending = False

            # I --> Insertion sort
            elif event.key == pygame.K_i and sorting == False:
                algorithm = insertion_sort
                algorithm_name = "Insertion Sort"

            # B --> Bubble sort
            elif event.key == pygame.K_b and sorting == False:
                algorithm = bubble_sort
                algorithm_name = "Bubble Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
