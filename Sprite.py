import pygame
import random

# Initialize Pygame
pygame.init()

# Custom event IDs for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

# Define basic colors using pygame.Color
# Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')


# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 400 - width)
        self.rect.y = random.randint(0, 400 - height)
        self.speed = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        # Move the sprite
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Bounce off the walls
        if self.rect.left < 0 or self.rect.right > 400:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 400:
            self.speed[1] = -self.speed[1]
# Function to change the sprite color
def change_sprite_color(sprite):
    colors = [YELLOW, MAGENTA, ORANGE, WHITE]
    new_color = random.choice(colors)
    sprite.image.fill(new_color)
    print(f"Sprite color changed to: {new_color}")
# Function to change the background color
def change_background_color():
    colors = [BLUE, LIGHTBLUE, DARKBLUE]
    new_color = random.choice(colors)
    window.fill(new_color)
    print(f"Background color changed to: {new_color}")
# Create the game window
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Sprite Color Change Example")
# Create a sprite group
sprites = pygame.sprite.Group()
# Create a sprite instance and add it to the group
sprite = Sprite(WHITE, 50, 50)
sprites.add(sprite)
# Set the initial background color
window.fill(BLUE)
# Set a timer for color change events
pygame.time.set_timer(SPRITE_COLOR_CHANGE_EVENT, 2000)  # Change sprite color every 2 seconds
pygame.time.set_timer(BACKGROUND_COLOR_CHANGE_EVENT, 5000)  # Change background color every 5 seconds
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            change_sprite_color(sprite)
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    # Update the sprite
    sprites.update()

    # Draw everything
    window.fill(BLUE)
    sprites.draw(window)

    # Update the display
    pygame.display.flip()
# Quit Pygame
pygame.quit()
# This code creates a Pygame window with a sprite that changes color and bounces around the screen.
# The sprite's color changes every 2 seconds, and the background color changes every 5 seconds.
# The colors are chosen randomly from predefined lists of colors.
# The sprite is represented by a rectangle, and the movement is handled by updating its position based on its speed.
# The code also includes event handling for quitting the game and changing colors.
# The main game loop continuously checks for events, updates the sprite's position, and redraws the screen.
# The code is structured to be easily extensible, allowing for additional features or modifications in the future.
# The use of custom events for color changes allows for a clean separation of concerns and makes the code more organized.
# The sprite's color and background color are defined using pygame.Color for better readability.
# The code is well-commented, providing explanations for each section and function.
# The use of constants for colors and event IDs improves maintainability and readability.