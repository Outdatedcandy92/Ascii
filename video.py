from PIL import Image
import numpy as np
import os
import time

import moviepy.editor as mp

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 32]
    return ascii_str

def convert_frame_to_ascii(frame, new_width=100):
    image = Image.fromarray(frame)
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index:index + img_width] for index in range(0, ascii_str_len, img_width)])

    return ascii_img

def video_to_ascii(video_path, new_width=100):
    video = mp.VideoFileClip(video_path)
    ascii_frames = []

    for frame in video.iter_frames():
        ascii_frame = convert_frame_to_ascii(frame, new_width)
        ascii_frames.append(ascii_frame)

    return ascii_frames

def play_ascii_video(ascii_frames, fps):
    os.system('cls' if os.name == 'nt' else 'clear')
    for frame in ascii_frames:
        print(frame)
        time.sleep(1 / fps)
        os.system('cls' if os.name == 'nt' else 'clear')

video_path = 'donut.gif'
ascii_frames = video_to_ascii(video_path, new_width=100)
play_ascii_video(ascii_frames, fps=24)
