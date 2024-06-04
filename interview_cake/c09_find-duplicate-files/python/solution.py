"""
You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all over your file system.
Even worse, she saved the duplicate files with random, embarrassing names.

Write a function that finds all the duplicate files.
To help confirm that two files are actually duplicates, return a list of tuples where first item is the duplicate file path and second is the original file path.
You can assume each file was only duplicated once.

Time: O(n)
Space: O(n)
"""

import hashlib
from pathlib import Path


def find_duplicates(directory: str) -> list[tuple[str]]:
    dups: list[tuple[str]] = []
    files: dict[str, tuple] = {}
    for file_path in Path(directory).rglob("*"):
        if file_path.is_file():
            abs_path = str(file_path.absolute())
            file_stats = file_path.stat()
            ts = int(file_stats.st_mtime)
            file_hash = sample_hash(abs_path, file_stats.st_size)
            if dup := files.get(file_hash):
                if int(ts) > dup[1]:
                    dups.append((abs_path, dup[0]))
                else:
                    dups.append((dup[0], abs_path))
            else:
                files[file_hash] = (abs_path, int(ts))
    return dups


def sample_hash(file_path: str, file_size: int) -> str:
    sample_size = 4000
    hasher = hashlib.md5()
    with open(file_path, "rb") as file:
        if file_size < sample_size * 3:
            hasher.update(file.read())
        else:
            sample_distance = (file_size - sample_size * 3) / 2
            for i in range(3):  # read start/middle/end sample parts
                sample_start = int(i * (sample_size + sample_distance))
                file.seek(sample_start)
                sample = file.read(sample_size)
                hasher.update(sample)
    return hasher.hexdigest()
