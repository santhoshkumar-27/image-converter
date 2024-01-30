import os
from PIL import Image

def create_thumbnail(input_path, output_folder, thumbnail_size=(100, 100), output_format="JPEG"):
    try:
        # Open the image file
        image = Image.open(input_path)

        # Create a thumbnail
        thumbnail = image.copy()
        thumbnail.thumbnail(thumbnail_size)

        # Extract the filename and extension
        filename, extension = os.path.splitext(os.path.basename(input_path))

        # Construct the output path for the thumbnail
        thumbnail_output_path = os.path.join(output_folder, f"{filename}_thumbnail.{output_format.lower()}")

        # Save the thumbnail with the specified format
        thumbnail.save(thumbnail_output_path, format=output_format)

        print(f"Thumbnail created successfully: {thumbnail_output_path}")

    except Exception as e:
        print(f"Error creating thumbnail: {e}")

def create_same_size_image(input_path, output_folder, output_format="JPEG"):
    try:
        # Open the image file
        image = Image.open(input_path)

        # Extract the filename and extension
        filename, extension = os.path.splitext(os.path.basename(input_path))

        # Construct the output path for the image with the same size
        output_path = os.path.join(output_folder, f"{filename}_converted.{output_format.lower()}")

        # Save the image with the specified format
        image.save(output_path, format=output_format)

        print(f"Image created successfully with the same size: {output_path}")

    except Exception as e:
        print(f"Error creating image with the same size: {e}")

def process_images(input_folder, output_folder, thumbnail_size=(100, 100), thumbnail_format="JPEG", same_size_format="JPEG"):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image (you can add more image formats if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            create_thumbnail(input_path, output_folder, thumbnail_size=thumbnail_size, output_format=thumbnail_format)
            create_same_size_image(input_path, output_folder, output_format=same_size_format)

if __name__ == "__main__":
    input_folder = "/home/tlspc-171/Pictures/geniemd"
    output_folder = "/home/tlspc-171/Pictures/geniemd/output"
    thumbnail_size = (100, 100)
    thumbnail_format = "JPEG"
    same_size_format = "WEBP"

    process_images(input_folder, output_folder, thumbnail_size=thumbnail_size, thumbnail_format=thumbnail_format, same_size_format=same_size_format)
