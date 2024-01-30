from PIL import Image
import sys

def create_thumbnail(input_path, output_path, thumbnail_size=(100, 100), output_format="JPEG"):
    try:
        # Open the image file
        image = Image.open(input_path)

        # Create a thumbnail
        thumbnail = image.copy()
        thumbnail.thumbnail(thumbnail_size)

        # Save the thumbnail with the specified format
        thumbnail.save(output_path, format=output_format)

        print(f"Thumbnail created successfully: {output_path}")

    except Exception as e:
        print(f"Error creating thumbnail: {e}")

def create_same_size_image(input_path, output_path, output_format="JPEG"):
    try:
        # Open the image file
        image = Image.open(input_path)

        # Save the image with the specified format
        image.save(output_path, format=output_format)

        print(f"Image created successfully with the same size: {output_path}")

    except Exception as e:
        print(f"Error creating image with the same size: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py input_image_path output_path output_format forThumbnail")
        # python im.py /home/tlspc-171/Pictures/geniemd/workspace.jpg /home/tlspc-171/Pictures/geniemd/workspace.gif gif 1
    else:
        input_image_path = sys.argv[1]
        output_path = sys.argv[2]
        output_format = sys.argv[3]
        forThumbnail = sys.argv[4].upper()

        if forThumbnail == "1":
            create_thumbnail(input_image_path, output_path)
        else:
            create_same_size_image(input_image_path, output_path, output_format=output_format)
