# ASCII Art Converter

Welcome to the ASCII Art Converter! This project allows you to convert images, videos, and camera feeds into ASCII art.

https://github.com/user-attachments/assets/d73647d0-b76e-4ee0-9a54-4104832a1854

## Project Structure

### Files
- **camera.py**: Captures video from the camera and converts it to ASCII art in real-time.
- **image.py**: Converts a static image to ASCII art.
- **main.py**: Main entry point for the application. Provides a menu to choose between converting camera feed, image, or video to ASCII art.
- **video.py**: Converts a video file to ASCII art.
- **requirements.txt**: Lists the dependencies required for the project.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Outdatedcandy92/Ascii.git
    cd Ascii
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Main Application

To start the main application, run:
```sh
python main.py
```
You will be presented with a menu to choose between converting camera feed, image, or video to ASCII art.

### Converting an Image to ASCII
To convert an image to ASCII art, run:

```sh
python image.py <image_path>
```

### Converting a Video to ASCII
To convert a video to ASCII art, run:

```sh
python video.py <video_path>
```

### Converting Camera Feed to ASCII
To convert the camera feed to ASCII art, run:

```sh
python camera.py
```

