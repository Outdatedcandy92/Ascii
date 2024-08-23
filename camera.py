import imageio
from PIL import Image
import numpy as np
import os
import time
import shutil

ASCII_CHARS = "@%#*+=-:.!@#$^&*()"
FPS = 60

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

def convert_frame_to_ascii(frame, new_width):
    image = Image.fromarray(frame)
    image = resize_image(image, new_width)
    ascii_str = pixels_to_ascii(image)
    return ascii_str

def main():
    terminal_size = shutil.get_terminal_size()
    terminal_width = terminal_size.columns

    print("Starting video capture...")
    try:
        reader = imageio.get_reader('<video0>')
        for frame in reader:
            frame = np.array(frame)
            frame = np.fliplr(frame)  
            ascii_frame = convert_frame_to_ascii(frame, new_width=terminal_width)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_frame)
            time.sleep(1 / FPS)  

    except KeyboardInterrupt:
        print("Exiting gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        reader.close()

if __name__ == "__main__":
    print("Starting program...")
    main()
    print("Program ended.")