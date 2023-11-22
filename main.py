import os

# Check for root user
if os.getuid() != 0:
    print("Please run script as root")
    exit(1)

# Hide pygame start screen
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
os.environ["SDL_AUDIODRIVER"] = "dsp"

import RPi.GPIO as GPIO
import pygame

# Use BCM mode for gpio pins
GPIO.setmode(GPIO.BCM)

# Pins which are used for expressions
pins = {
    "happy": 5,
    "sad": 6,
    "angry": 13,
    "tired": 19,
    "broken": 26,
    "surprised": 21,
    "skeptical": 20,
    "love": 16,
}

# Set pins as pull down (connect to 5v to trigger)
for pin in pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Only update display 60 times per second
FPS = 60

# Initialize 24-bit color mode
os.system("fbset -depth 24")
pygame.init()

# Initialize pygame screen
size = (656, 512)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Move mouse off screen
pygame.mouse.set_pos(size)
pygame.display.flip()


def draw_expression(name):
    # Load expression image
    path = f"screens/{name}.png"
    expression = pygame.image.load(path)
    expression_rect = expression.get_rect()

    # Display image on screen
    screen.blit(expression, expression_rect)


def get_pinstates():
    # Get pin states of each pin
    states = {}
    for name, pin in pins.items():
        states[name] = GPIO.input(pin)

    # Return new pin states
    return states


# Main loop
done = False
while not done:
    # Clear screen before updates
    clock.tick(FPS)
    screen.fill(BLACK)

    # Exit loop when quit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Display expression based on numkeys or pins (default = neutral)
    pinstates = get_pinstates()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        # Quit if 'q' key pressed
        done = True
    elif keys[pygame.K_1] or pinstates["happy"]:
        draw_expression("happy")
    elif keys[pygame.K_2] or pinstates["sad"]:
        draw_expression("sad")
    elif keys[pygame.K_3] or pinstates["angry"]:
        draw_expression("angry")
    elif keys[pygame.K_4] or pinstates["tired"]:
        draw_expression("tired")
    elif keys[pygame.K_5] or pinstates["broken"]:
        draw_expression("broken")
    elif keys[pygame.K_6] or pinstates["surprised"]:
        draw_expression("surprised")
    elif keys[pygame.K_7] or pinstates["skeptical"]:
        draw_expression("skeptical")
    elif keys[pygame.K_8] or pinstates["love"]:
        draw_expression("love")
    else:
        draw_expression("neutral")

    # Update display
    pygame.display.flip()

# Cleanup
pygame.quit()
GPIO.cleanup()
