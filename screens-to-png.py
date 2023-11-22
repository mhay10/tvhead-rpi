from PIL import Image
from glob import glob
import os

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Size of screen
WIDTH = 656
HEIGHT = 512

# Get all screens
screens = glob("screens/*.txt")
for screen in screens:
    # Create image same size as screen
    img = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = img.load()

    # Loop through screen and set pixels
    with open(screen) as f:
        y = 0
        for line in f.readlines():
            line = line.strip()

            x = 0
            for c in line:
                # Set pixel to white if 1, black if 0
                pixels[x, y] = WHITE if c == "1" else BLACK
                x += 1

            y += 1

    # Save image as PNG in same directory
    basename = os.path.basename(screen)
    filename = os.path.splitext(basename)[0]
    img.save(f"screens/{filename}.png", "PNG")
