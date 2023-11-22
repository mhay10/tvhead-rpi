from PIL import Image
import sys
import os

# Make sure program has right number of arguments
if len(sys.argv) != 4:
    print(f"Usage: {os.path.basename(sys.argv[0])} <left eye> <right eye> <save name>")
    exit(1)

# Positions of eyes on screen
LEFTPOS = (115, 210)
RIGHTPOS = (440, 210)

# Size of eyes on screen
EYESIZE = (96, 96)

# Create screen
width, height = 656, 512
screen = Image.new("L", (width, height))

# Load eyes and convert to grayscale
left = Image.open(sys.argv[1]).convert("L")
right = Image.open(sys.argv[2]).convert("L")

# Resize eyes and paste onto screen
screen.paste(left.resize(EYESIZE, resample=Image.Resampling.NEAREST), LEFTPOS)
screen.paste(right.resize(EYESIZE, resample=Image.Resampling.NEAREST), RIGHTPOS)

# Create directory for screens if it doesn't exist
os.makedirs("screens", exist_ok=True)

# Save screen as text file of 0 and 1
with open(f"screens/{sys.argv[3]}.txt", "w") as f:
    # Loop through pixels and write 0 if black, 1 if white
    pixels = screen.load()
    for y in range(screen.height):
        for x in range(screen.width):
            f.write("0" if pixels[x, y] < 255 else "1")
        f.write("\n")
