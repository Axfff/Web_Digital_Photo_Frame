import os
from PIL import Image


def resize_image(input_image_path, output_image_path, max_size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} tall")

    if width > height:
        new_width = max_size
        new_height = int(height * (max_size / width))
    else:
        new_width = int(width * (max_size / height))
        new_height = max_size

    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    resized_image.save(output_image_path, optimize=True, quality=60)
    print(f"The resized image size is {new_width} wide x {new_height} tall")


def process_directory(input_directory, output_directory, max_size):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            resize_image(input_path, output_path, max_size)


if __name__ == '__main__':
    process_directory("materials/Archive/JGA2023/showphotos",
                      "materials/Archive/JGA2023/showphotos/converted",
                      1280)
