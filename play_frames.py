import pygame
import os
import time

# Initialize pygame
pygame.init()

# Set the folder path
folder_path = 'left'

# Get all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif'))]
image_files.sort()  # Sort the files alphabetically

# Set display dimensions
display_width = 1920
display_height = 1080

# Create a pygame display
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Image Slideshow')

# Set the frame rate (frames per second)
fps = 140
clock = pygame.time.Clock()

# Option to start from a higher indexed image
start_index = 65000  # Change this value to start from a different image index

def show_image(image_path):
    # Load and scale the image
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (display_width, display_height))
    screen.blit(image, (0, 0))

    # Display the filename at the top of the screen
    font = pygame.font.Font(None, 36)
    text = font.render(os.path.basename(image_path), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

def main():
    running = True
    paused = False
    # Ensure start_index is within the bounds of image_files
    current_image_index = start_index % len(image_files)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Spacebar to pause/unpause
                    paused = not paused

        if not paused:
            if current_image_index < len(image_files):
                image_path = os.path.join(folder_path, image_files[current_image_index])
                show_image(image_path)
                current_image_index = (current_image_index + 1) % len(image_files)  # Loop back to the first image if necessary

            time.sleep(0.0001)  # Display each image for 1 second

        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()
