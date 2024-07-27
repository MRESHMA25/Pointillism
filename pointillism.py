# pointillism.py
# Full Name: Reshma Sri Murakonda
# Student Number: 101282055

import pygame
import random
import sys

def main():
    # Initialize pygame
    pygame.init()

    # Load the source image
    source_image_path = "image.jpg"  # Assumes the image is named "image" in the same directory
    try:
        source_image = pygame.image.load(source_image_path)
    except pygame.error:
        print(f"Unable to load image: {source_image_path}")
        print("Make sure the image file is in the same directory as this script.")
        sys.exit(1)

    source_width, source_height = source_image.get_size()

    # Set the scaling factor between 4 and 8
    scaling_factor = 6

    # Calculate new image dimensions
    new_width = source_width * scaling_factor
    new_height = source_height * scaling_factor

    # Create a new surface for the scaled-up image
    new_image = pygame.Surface((new_width, new_height))
    new_image.fill((255, 255, 255))  # Fill with white background

    # Define the colors
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Function to draw a point
    def draw_point(surface, color, x, y, size=3):
        shape = random.choice(['circle', 'square', 'rectangle'])
        if shape == 'circle':
            pygame.draw.circle(surface, color, (x, y), size)
        elif shape == 'square':
            pygame.draw.rect(surface, color, (x-size//2, y-size//2, size, size))
        elif shape == 'rectangle':
            pygame.draw.rect(surface, color, (x-size, y-size//2, size*2, size))

    # Visit each pixel in the source image
    for y in range(source_height):
        for x in range(source_width):
            color = source_image.get_at((x, y))

            # Determine the number of points to draw based on the color
            red_points = color.r // 64
            green_points = color.g // 64
            blue_points = color.b // 64

            # Draw points
            for _ in range(red_points):
                new_x = x * scaling_factor + random.randint(0, scaling_factor - 1)
                new_y = y * scaling_factor + random.randint(0, scaling_factor - 1)
                draw_point(new_image, RED, new_x, new_y)

            for _ in range(green_points):
                new_x = x * scaling_factor + random.randint(0, scaling_factor - 1)
                new_y = y * scaling_factor + random.randint(0, scaling_factor - 1)
                draw_point(new_image, GREEN, new_x, new_y)

            for _ in range(blue_points):
                new_x = x * scaling_factor + random.randint(0, scaling_factor - 1)
                new_y = y * scaling_factor + random.randint(0, scaling_factor - 1)
                draw_point(new_image, BLUE, new_x, new_y)

    # Save the new image
    pygame.image.save(new_image, 'result.png')
    print("Pointillist image saved as 'result.png'")

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
