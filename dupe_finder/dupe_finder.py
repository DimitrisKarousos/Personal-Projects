"""Module that notifies the user for duplicate filepaths in a path tree"""
import os

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
target = os.getenv('TRGT')

def find_dupes(show_confidence = False):
    """Finds duplicate filepaths in the a given tree, displays the paths if any"""
    paths = Path(target).rglob('*')
    filepaths = []
    dupes = []
    for p in paths:
        if p .is_file():
            filepaths.append(p)
    n = len(filepaths)
    for i in range(n):
        for j in range(i + 1, n):
            certainty = 0
            if filepaths[i].stat().st_size == filepaths[j].stat().st_size:
                certainty += 1
            if filepaths[i].name == filepaths[j].name:
                certainty += 1
                dupes.append((filepaths[i], filepaths[j], certainty))
    if not dupes:
        print("No duplicate files found.")
    else:
        print("Duplicates found:")
        for dupe in dupes:
            print(f'{dupe[0].name} in\n{dupe[0].parent} and {dupe[1].parent}')
            if show_confidence:
                print(f'with a confidence of {dupe[2]}')

if __name__ == "__main__":
    find_dupes(True)
