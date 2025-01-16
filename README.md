# File Unzipping and Zipping Utility

A command-line tool for compressing and decompressing files and folders in various formats, built with Python and Typer.

## Features
- Create `.zip` files from folders or files.
- Extract `.zip`, `.rar`, and `.7z` files.
- Specify custom destination folders for extraction.

## Installation
1. Clone the repository:
git clone https://github.com/johncullinane401/cli-zip-app

2. Install the dependencies:
pip install typer py7zr rarfile

### Usage
Ensure your pwd is the directory where the zipmanager.py is located.

# Compress a file/folder to .zip
python zipmanager.py file-to-zip <source_path> <destination_path>

# Unzip .zip file contents to current directory
python zipamanager.py unzip-here <source_path> 

# Unzip .zip file contents to a new folder in current directory
python zipamanager.py unzip-here <source_path> <folder_name>

# Unzip a .rar file contents to a new folder in the current directory
python zipmanager.py unzip-rar <source_path> <folder_name>

# Unzip a .7z file contents to a new folder in the current directory
python zipmanager.py unzip-rar <source_path> <folder_name>

# License
This project is licensed under the MIT License.
