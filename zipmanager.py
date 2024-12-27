import py7zr.py7zr
import typer
import zipfile
import rarfile
import os
import py7zr

from pathlib import Path

app = typer.Typer()


"""
Function for Zipping a File or Folder
@param 
"""
@app.command(help="Converts a folder or file into a new .zip file")
def file_to_zip(source: Path, destination: Path):

    # check if the given file path exists; if it doesnt we throw an error
    if not source.exists():
        print("The designated file path does not exist. Please try again and/or double check your spelling.")
        raise typer.Exit(code=1)
    
    # check if the provided output file name contains a .zip
    # if it doesnt we append it to the end
    if destination.suffix != ".zip":
        destination = Path(str(destination) + ".zip")
    
    # create the object for unzipping
    zip_device = zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED)
    for filename in os.listdir(source):
        file_path = source / filename
        if file_path.is_file():
            zip_device.write(file_path, filename)
    zip_device.close()
    print("Successfully zipped file contents to", destination)
    return

# Code for unzipping a file
@app.command(help="Unzips and exports the contents of .zip file to the current directory")
def unzip_here(source: Path):
    
    # check if the given file path exists; if it doesn't we throw an error
    if not source.exists():
        print("The designated file path does not exist. Please try again and/or double check your spelling.")
        raise typer.Exit(code=1)
    
    # check if the provided file leads to a zip file
    if source.suffix != ".zip":
        print("The given source file is not a .zip file. Please try again")
        raise typer.Exit(code=2)
    
    # set the destination as the current working directory
    destination = Path.cwd()

    # unzip to the current working directory
    zip_device = zipfile.ZipFile(source, "r")
    zip_device.extractall(destination)
    zip_device.close()

    # print a message to let the user know it worked successfuly
    print("Successfully unzipped file contents to", destination)
    return

@app.command(help="Unzips a .zip file to a new folder in current directory")
def unzip_to_folder(source: Path, folder_name: str):
    
    # check if the given file path exists; if it doesn't we throw an error
    if not source.exists():
        print("The designated file path does not exist. Please try again and/or double check your spelling.")
        raise typer.Exit(code=1)
    
    # check if the provided file leads to a zip file
    if source.suffix != ".zip":
        print("The given source file is not a .zip file. Please try again")
        raise typer.Exit(code=2)
    
    # create a new folder with the given destination name
    temp_dir = Path.cwd() / folder_name
    temp_dir.mkdir(exist_ok=True)
    
    # unzip to the new folder
    zip_device = zipfile.ZipFile(source, "r")
    zip_device.extractall(temp_dir)
    zip_device.close()

    # output a message to inform the user that it successfuly extracted to the new folder
    print(f"Successfully unzipped file contents to", temp_dir)
    return

## Unzips a rar file to a designated folder
@app.command(help="Unzips a .rar file to a new folder in current directory")
def unzip_rar(source: Path, folder_name: str):
    # check if the provided file leads to a file that exists, if not throw an error
    if not source.exists():
        print("The designated file path does not exist. Please try again and/or double check your spelling.")
        raise typer.Exit(code=1)
    
    # check if the 
    if source.suffix != ".rar":
        print("The given source file is not a .zip file. Please try again")
        raise typer.Exit(code=2)
    
    # Create a new folder with the specified name
    temp_dir = Path.cwd() / folder_name
    temp_dir.mkdir(exist_ok=True)
    
    # Unzip to the new folder
    rar_device = rarfile.RarFile(source, "r")
    rar_device.extractall(temp_dir)
    rar_device.close()
    print(f"Successfully unzipped file contents to", temp_dir)
    return


## Unzips a 7z file to a designated folder
@app.command()
def unzip_7z(source: Path, folder_name: str):
    # check if the provided file leads to a file that exists, if not throw an error
    if not source.exists():
        print("The designated file path does not exist. Please try again and/or double check your spelling.")
        raise typer.Exit(code=1)
    
    # check if the 
    if source.suffix != ".7z":
        print("The given source file is not a .zip file. Please try again")
        raise typer.Exit(code=2)
    
    # Create a new folder with the specified name
    temp_dir = Path.cwd() / folder_name
    temp_dir.mkdir(exist_ok=True)
    
    # Unzip to the new folder
    #z_device = py7zr.7zFile(source, "r")
    #z_device.extractall(temp_dir)
    #z_device.close()
    print(f"Successfully unzipped file contents to", temp_dir)
    return

app()