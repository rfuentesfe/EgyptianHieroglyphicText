import os
import subprocess
import shutil

# Repository URL
repo_url = "https://github.com/rfuentesfe/EgyptianHieroglyphicText.git"
repo_clone_dir = "EgyptianHieroglyphicText"
target_dir = "GlyphHiero2025"

# Step 1: Clone the repository
if not os.path.exists(repo_clone_dir):
    print("Cloning the repository...")
    subprocess.run(["git", "clone", repo_url])
else:
    print("The repository has already been cloned.")

# Step 2: Verify the existence of the 'dataset' folder
dataset_path = os.path.join(repo_clone_dir, "dataset")
if not os.path.exists(dataset_path):
    raise FileNotFoundError("The 'dataset' folder was not found in the repository.")

# Step 3: Move the 'dataset' folder to the root and rename it
if os.path.exists(target_dir):
    shutil.rmtree(target_dir)  # Remove the destination if it already exists
shutil.move(dataset_path, target_dir)

print(f"The 'dataset' folder has been moved and renamed to '{target_dir}'.")
