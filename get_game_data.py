import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game" # Pattern to identify game directories
GAME_COMPILE_COMMAND = ["go", "build"]  # Command to compile Go code


def find_all_game_path(source):
    game_paths = []
    for root, dirs, files in os.walk(source):
        for dir_name in dirs:
            if GAME_DIR_PATTERN in dir_name.lower():
                game_paths.append(os.path.join(root, dir_name))
        break  # Prevent descending into subdirectories
    return game_paths


def get_name_from_path(path,strip):
    new_names = []
    for path in path:
        _, dirname= os.path.split(path)
        newname= dirname.replace(strip,"")
        new_names.append(newname)
    return new_names


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def copy(source, target):
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)


def json_metadata(path, dir_names):
    data ={
        "GameNames":dir_names,
        "no_of_games": len(dir_names)
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def compile_game(path):
    code_file = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".go"):
                code_file = file
                break
    if code_file is None:
        return
    compile_command = GAME_COMPILE_COMMAND + [code_file]
    run_command(compile_command, path)


def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)
    try:
        process = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        print("compile results", process)
    except FileNotFoundError:
        print(f"Error: '{command[0]}' command not found. Please ensure Go is installed and added to PATH.")
    finally:
        os.chdir(cwd)
    


def main(source, target):
    cwd=os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_path = find_all_game_path(source_path)
    newnames = get_name_from_path(game_path, "_game")
    create_dir(target_path) 
    for src, dec in zip(game_path, newnames):
        dest_path = os.path.join(target_path,dec)
        copy(src, dest_path)
        compile_game(dest_path)
    
    jsonp=os.path.join(target_path, "metadata.json")
    json_metadata(jsonp, newnames)
    
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Usage: python get_game_data.py <source_directory> <destination_directory>")
    source_dir = args[1]
    dest_dir = args[2]
    main(source_dir, dest_dir)