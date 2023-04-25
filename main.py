import os
import shutil
import subprocess

def get_terminal_size():
    # Get the width and height of the terminal dynamically
    size = shutil.get_terminal_size((80, 20))
    if size.columns == 80 and size.rows == 20:
        # If the size is still the default value, try to get the actual size using stty
        try:
            size = subprocess.check_output(['stty', 'size']).decode().split()
            size = (int(size[1]), int(size[0]))
        except:
            pass
    return size

def list_files(path="."):
    # Get the list of files in the specified directory
    files = os.listdir(path)
    # Get the size of the terminal dynamically
    terminal_size = get_terminal_size()
    # Calculate the maximum filename length
    max_len = max(len(file) for file in files) + 2
    # Calculate the number of columns
    num_cols = terminal_size.columns // max_len
    # Print the list of files in columns
    for i in range(0, len(files), num_cols):
        row = files[i:i+num_cols]
        print(" ".join(file.ljust(max_len) for file in row))

# Example usage
list_files()
