"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:

    list_of_files = list(dir_path.glob("*." + file_extension))
    if tokenizer is None:
        counter_of_lines = 0
        for file in list_of_files:
            with open(file) as f:
                counter_of_lines += len(f.readlines())
        return counter_of_lines
    else:
        counter_of_tokens = 0
        for file in list_of_files:
            with open(file) as f:
                counter_of_tokens += len(list(map(tokenizer, f.readlines())))
        return counter_of_tokens


print(universal_file_counter(Path.cwd() / "test_dir", "txt", str.split))
