from task03.hw3 import *


def test_call_without_tokenizer():
    assert universal_file_counter(Path.cwd().parent / "task03" / "test_dir", "txt") == 6


def test_call_with_tokenizer():
    assert (
        universal_file_counter(
            Path.cwd().parent / "task03" / "test_dir", "txt", str.split
        )
        == 6
    )
