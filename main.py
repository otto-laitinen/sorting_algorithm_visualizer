import pygame

from draw import draw
from DrawInformation_class import DrawInformation
from generate_list import generate_initial_list
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

# Event loop
def main():
    run = True
    clock = pygame.time.Clock()

    n = 50  # Number of items
    min_value = 0
    max_value = 100

    # Generate initial list
    lst = generate_initial_list(n, min_value, max_value)

    # Draw the window
    draw_info = DrawInformation(700, 700, lst)

    # Default algorithm properties
    algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    algorithm_generator = None
    ascending = True
    sorting = False

    while run:
        clock.tick(120)  # Speed of the algorithm

        if sorting:
            try:
                next(algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, algorithm_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            # R --> Generate a random list
            if event.key == pygame.K_r:
                lst = generate_initial_list(n, min_value, max_value)
                draw_info.set_list(lst)
                sorting = False

            # Enter --> Start sorting
            elif event.key == pygame.K_RETURN and sorting == False:
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
