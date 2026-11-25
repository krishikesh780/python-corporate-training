
"""
Module: a single .py file that defines functions, classes, variables. 
Example: salary.py.

Package: a directory that groups modules.
Historically contains init.py (now optional for namespace packages).
Example: finance/ with salary.py, tax.py, main.py
"""

# ==============================
#  OS Module: File Handling: Path Handling with Real Use
# ==============================

import os

# # os.path example

# ./file means "file in the current directory".
# ../file means "file in the parent directory" (one level up).
# ../../file means "file two levels up". It does NOT mean  or "downward".

# --------------------------------------
# 1. Absolute vs Relative Path
# --------------------------------------
# Absolute path = Full system path

def print_path_info():

    full_path= os.path.abspath(__file__)  # Full path of current script
    print("Full Path of Current Script:", full_path)
    
    absolute_path = r"D:\python_corporate_training\sample.txt"   # Windows Example
    # print("Absolute Path:", absolute_path)
    # absolute_path2 = r"D:\python_corporate_training\week1\ex.py"  # Linux/Mac Example


    # print("Full Path of Current Script:", full_path)
    # print("Absolute Path :", absolute_path)

    # Relative path = relative to current script
    # full_path= os.path.abspath(__file__)  # Full path of current script
    current_dir = os.path.dirname(full_path)  # Directory of Current Script
    print("Current Dir:", current_dir)
    
    
    rel = os.path.relpath(absolute_path, start=current_dir)  # Relative path from current dir to absolute_path
    # rel = os.path.relpath(absolute_path2, start=current_dir)  # Relative path from current dir to absolute_path

    print(rel)  # -> ..\..\sample.txt on Windows

# print_path_info()

# 2.  Path Join (Safe Way to Create Paths)
# Instead of manually writing "folder/file.txt", use os.path.join

# --------------------------------------
def safe_path_join(*args):
    
    #project root: D:\python_corporate_training 
    base_dir = os.getcwd()
    print("Base Dir:", base_dir)
    folder_name = "myfolder"
    file_name = "data.txt"

    # # Join folder + filename
    joined_path = os.path.join(base_dir, folder_name, file_name)
    print("Joined Path:", joined_path)


safe_path_join()



# 3. Create Folder + File inside it
# --------------------------------------
def create_folder_and_file():
    base_dir = os.getcwd()
    new_folder = "new_data_folder"
    new_file = "info.txt"

    # Create full path for new folder
    folder_path = os.path.join(base_dir, new_folder)
    os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

    # Create full path for new file
    file_path = os.path.join(folder_path, new_file)
    with open(file_path, 'w') as f:
        f.write("This is some sample text.")

    print(f"Created folder at: {folder_path}")
    print(f"Created file at: {file_path}")


# create_folder_and_file()


# 4. user-define
 # expmales of os.path and pathlib for path manipulations

def print_os_path_examples():
   
    cwd = os.getcwd()               # current working directory
    print("cwd:", cwd)

    p1 = os.path.join(cwd, "file1.py")       # ./file1.py resolved against cwd
    p2 = os.path.abspath(os.path.join(cwd, "..", "file2.py"))   # ../file2.py
    p3 = os.path.abspath(os.path.join(cwd, "..", "..", "file3.py"))  # ../../file3.py

    print("file1 ->", p1)
    print("file2 ->", p2)
    print("file3 ->", p3)

# print_os_path_examples()


#  Request Module:

