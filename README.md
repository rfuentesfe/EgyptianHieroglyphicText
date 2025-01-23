# Egyptian Hieroglyphic Dataset

This repository contains the dataset and accompanying resources for the study and recognition of Egyptian hieroglyphic texts. The dataset was developed as part of the research conducted in the following paper:

## Citation  
R. Fuentes-Ferrer, J. Duque-Domingo, and P.J. Herrera (2025). *Recognition of Egyptian Hieroglyphic Texts through Focused Generic Segmentation and Cross-Validation Voting*. Applied Soft Computing, DOI: https://doi.org/10.1016/j.asoc.2025.112793

## Dataset  <br>
Our dataset consists of 310 classes and 13,729 images, representing hieroglyphs on different materials, concretely carved or painted stone stelae. The hieroglyphs have been grouped in folders according to the structure and typology defined by the Egyptologist Gardiner.

Folder <br>
&nbsp;&nbsp;&nbsp;&nbsp; I ---- a1 -  Subgroup A1 (seated man) <br>
&nbsp;&nbsp;&nbsp;&nbsp; I ---- a2 -  Subgroup A2 (man with hand to mouth) <br>
&nbsp;&nbsp;&nbsp;&nbsp; I ---- a3 -  Subgroup A3 (man sitting on heel) <br>
&nbsp;&nbsp;&nbsp;&nbsp; I ...<br>
&nbsp;&nbsp;&nbsp;&nbsp; I ---- b1 -  Subgroup B1 (seated woman) <br>
&nbsp;&nbsp;&nbsp;&nbsp; I ...<br>
&nbsp;&nbsp;&nbsp;&nbsp; I ---- z1 -  Subgroup Z1 (single stroke) <br>
&nbsp;&nbsp;&nbsp;&nbsp; I ... <br>
 
We encourage researchers who use this dataset in their work to cite our paper in their publications. Once the DOI, volume, and page numbers are available, this reference will be updated accordingly.

## Overview

This project provides tools for managing datasets of Egyptian hieroglyphs. The pipeline includes:
- Downloading datasets from public and private sources.
- Merging datasets into a unified structure.
- Adjusting image sizes for training machine learning models.

The resulting dataset is stored in a single folder called `Glyph2025`.

## Scripts

### 1. Download Franken Dataset

This script downloads the Egyptian Hieroglyph Dataset provided at `http://jvgemert.github.io/pub/EgyptianHieroglyphDataset.tar.gz`. It performs the following tasks:
- Downloads and extracts the dataset.
- Reorganizes files from the `test` folder into the `train` folder based on their naming convention.
- Renames the `train` folder to `GlyphFranken2025` and deletes unnecessary files.

**Script**: `1_download_franken_dataset.py`

### 2. Download Our Dataset

This script clones a private dataset repository from GitHub. It performs the following tasks:
- Clones the repository containing hieroglyph datasets.
- Extracts the `dataset` folder.
- Renames it to `GlyphHiero2025`.

**Script**: `2_download_our_dataset.py`

### 3. Merge Datasets

This script merges the datasets from `GlyphFranken2025` and `GlyphHiero2025` into a single unified structure named `Glyph2025`. It:
- Copies files while maintaining the structure of both datasets.
- Converts all file and folder names to lowercase to ensure consistency.

**Script**: `3_merge_datasets.py`

### 4. Adjust Files

This script adjusts the size of all images in the `Glyph2025` dataset to a uniform size of `224x224` pixels. It:
- Resizes images while preserving the aspect ratio.
- Adds black padding to fill the remaining space.
- Replaces the original images with the adjusted versions.

**Script**: `4_adjust_files.py`

## Requirements

To run the scripts, you need the following dependencies installed on your system:

- Python 3.6 or higher
- Pillow
- Git
- Required Python libraries:
  ```bash
  pip install pillow

## Usage

Run the scripts in the following order:

1. Download Franken Dataset:

   ```bash
   python 1_download_franken_dataset.py

2. Download Our Dataset:
 
   ```bash
   python 2_download_our_dataset.py

3. Merge Datasets:

   ```bash
   python 3_merge_datasets.py

4. Adjust Files:

   ```bash
   python 4_adjust_files.py

The final dataset will be available in the Glyph2025 folder.
