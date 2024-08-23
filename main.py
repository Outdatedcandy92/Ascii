import subprocess

def main():
    print("Welcome to ASCII Art Converter!")
    print("Please choose an option:")
    print("1. Convert Camera Feed to ASCII")
    print("2. Convert Image to ASCII")
    print("3. Convert Video to ASCII")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        subprocess.run(["python", "camera.py"])
    elif choice == "2":
        image_path = input("Enter the path to the image: ")
        subprocess.run(["python", "image_to_ascii.py", image_path])
    elif choice == "3":
        video_path = input("Enter the path to the video: ")
        subprocess.run(["python", "video_to_ascii.py", video_path])
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()