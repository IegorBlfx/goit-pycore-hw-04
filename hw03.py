import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)  # Reset color after each print


def print_tree(directory, indent=1):  # Recursively print directory contents
    try:
        items = sorted(directory.iterdir())
    except PermissionError:  # No access to directory
        print("    " * indent + Fore.RED + "[access denied]")
        return
    for item in items:
        if item.is_dir():
            print("    " * indent + Fore.BLUE + item.name + "/")  # Directories in blue
            print_tree(item, indent + 1)
        else:
            print("    " * indent + Fore.GREEN + item.name)  # Files in green


def main():
    if len(sys.argv) < 2:  # Path was not passed
        print(Fore.RED + "Usage: python hw03.py <path_to_directory>")
        return

    path = Path(sys.argv[1])
    if not path.is_dir():  # Path does not exist or is not a directory
        print(Fore.RED + f"No such directory: {path}")
        return

    print(Fore.BLUE + path.resolve().name + "/")
    print_tree(path)


if __name__ == "__main__":
    main()
