from PIL import Image
import glob
import os

# Base path of the Glyph2025 folder
root_dir = "Glyph2025"
final_size = 224

# Function to process PNG and JPG images
def resize_and_replace_images():
    # Allowed extensions
    extensions = ['.png', '.jpg']

    # Search and process files with the allowed extensions
    for ext in extensions:
        for filename in glob.iglob(root_dir + f'/**/*{ext}', recursive=True):
            print(f"Processing: {filename}")
            im = Image.open(filename)
            size = im.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x * ratio) for x in size])
            im = im.resize(new_image_size, Image.LANCZOS)  # Resize the image
            new_im = Image.new("RGB", (final_size, final_size), color=(0, 0, 0))  # Create image with black background
            new_im.paste(im, ((final_size - new_image_size[0]) // 2, (final_size - new_image_size[1]) // 2))

            # Generate the new file name
            new_filename = filename  # Keep the same name as the original file
            new_im.save(new_filename)
            print(f"Saved: {new_filename}")

# Run the function to process all images
resize_and_replace_images()
