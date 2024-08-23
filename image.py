import sys
import numpy as np
from PIL import Image
import os
import shutil

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def pixels_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for pixel in pixels:
        for r, g, b in pixel:
            brightness = int((r + g + b) / 3)
            char = ASCII_CHARS[brightness // 32]
            ascii_str += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        ascii_str += "\n"
    return ascii_str

def convert_image_to_ascii(image_path):
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    print("Starting image conversion...")
    try:
        image = Image.open(image_path)
        image = resize_image(image, new_width=terminal_width)
        ascii_str = pixels_to_ascii(image)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_str)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image.py <image_path>")
    else:
        image_path = sys.argv[1]
        convert_image_to_ascii(image_path)