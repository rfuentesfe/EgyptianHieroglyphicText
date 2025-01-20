import os
import shutil

# Paths of the folders to merge
folder1 = "GlyphFranken2025"
folder2 = "GlyphHiero2025"
merged_folder = "Glyph2025"

# Create the destination folder if it doesn't exist
os.makedirs(merged_folder, exist_ok=True)

# Function to copy files and convert names to lowercase
def merge_folders_with_lowercase(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        # Get the relative path to maintain the structure
        relative_path = os.path.relpath(root, src_folder)
        relative_path_lower = relative_path.lower()  # Convert to lowercase
        target_path = os.path.join(dest_folder, relative_path_lower)

        # Create directories in the destination folder if they don't exist
        os.makedirs(target_path, exist_ok=True)

        # Copy files with lowercase names
        for file in files:
            src_file = os.path.join(root, file)
            file_lower = file.lower()  # Convert to lowercase
            dest_file = os.path.join(target_path, file_lower)
            if not os.path.exists(dest_file):  # Avoid overwriting
                shutil.copy2(src_file, dest_file)

# Merge the two folders
print(f"Merging '{folder1}' into '{merged_folder}'...")
merge_folders_with_lowercase(folder1, merged_folder)
print(f"Merging '{folder2}' into '{merged_folder}'...")
merge_folders_with_lowercase(folder2, merged_folder)

print(f"Merge completed! The combined folder is named '{merged_folder}', and all names are in lowercase.")
