import requests
from PIL import Image, ImageDraw, ImageFont
import random

# Config
WIDTH, HEIGHT = 800, 400
CELL_SIZE = 15
FRAMES = 25
USERNAME = "LorenzoCammarano"

# Recupera i contributi dall’API GitHub
url = f"https://github.com/users/{USERNAME}/contributions"
svg = requests.get(url).text

# Font monospace (default PIL)
font = ImageFont.load_default()
frames = []

for frame_idx in range(FRAMES):
    img = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Effetto pioggia Matrix
    for x in range(0, WIDTH, CELL_SIZE):
        y = random.randint(0, HEIGHT)
        char = random.choice("01░▒▓")
        green = random.randint(150, 255)
        draw.text((x, y), char, font=font, fill=(0, green, 70))

    frames.append(img)

# Salva GIF
frames[0].save("matrix_contributions.gif",
               save_all=True,
               append_images=frames[1:],
               duration=150,
               loop=0)
print("✅ Matrix GIF generata con successo!")
