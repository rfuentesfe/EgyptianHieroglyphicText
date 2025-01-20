import os
import tarfile
import urllib.request
import shutil

# URL of the compressed file
url = "http://jvgemert.github.io/pub/EgyptianHieroglyphDataset.tar.gz"
compressed_file = "EgyptianHieroglyphDataset.tar.gz"
extracted_dir = "EgyptianHieroglyphDataset"

# Step 1: Download the file
if not os.path.exists(compressed_file):
    print("Downloading the file...")
    urllib.request.urlretrieve(url, compressed_file)
else:
    print("The file has already been downloaded.")

# Step 2: Extract the file
if not os.path.exists(extracted_dir):
    print("Extracting the file...")
    with tarfile.open(compressed_file, "r:gz") as tar:
        tar.extractall()
else:
    print("The file has already been extracted.")

# Step 3: Verify base path and directories
base_path = os.path.join(extracted_dir, "ExampleSet7")
test_dir = os.path.join(base_path, "test")
train_dir = os.path.join(base_path, "train")

if not os.path.exists(base_path):
    raise FileNotFoundError("The 'ExampleSet7' folder was not found in the extracted data.")
if not os.path.exists(test_dir) or not os.path.exists(train_dir):
    raise FileNotFoundError("The 'test' or 'train' folders were not found inside 'ExampleSet7'.")

# Step 4: Reorganize files from test into train
print("Reorganizing files from 'test' to 'train'...")
for file in os.listdir(test_dir):
    if file.endswith(".png"):  # Check file format
        file_parts = file.split("_")
        if len(file_parts) < 2:
            continue  # Skip files with unexpected format
        
        target_folder_name = file_parts[1].split(".")[0]  # Extract target folder name
        target_folder_path = os.path.join(train_dir, target_folder_name)
        
        # Create folder in train if it doesn't exist
        os.makedirs(target_folder_path, exist_ok=True)
        
        # Move file
        source_file = os.path.join(test_dir, file)
        destination_file = os.path.join(target_folder_path, file)
        shutil.move(source_file, destination_file)

print("Files have been successfully reorganized!")

# Step 5: Move train folder to the root with the new name
glyph_dir = "GlyphFranken2025"
if os.path.exists(train_dir):
    shutil.move(train_dir, glyph_dir)
    print(f"The 'train' folder has been moved to the root and renamed to '{glyph_dir}'.")
else:
    print("The 'train' folder was not found to move.")

# Step 6: Delete the EgyptianHieroglyphDataset folder
if os.path.exists(extracted_dir):
    print("Deleting the EgyptianHieroglyphDataset folder...")
    shutil.rmtree(extracted_dir)
    print("The EgyptianHieroglyphDataset folder has been deleted.")
else:
    print("The EgyptianHieroglyphDataset folder does not exist or has already been deleted.")
