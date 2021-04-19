"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import re


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode_escape") as f:
        # preparing list of words, deleting useless symbols
        text = f.read()
        text = re.sub("\n", "", text)
        text = re.sub("[-.,:;!?]", " ", text)
        words = [i.lower() for i in text.split(" ") if i != ""]
        # creating dict. key - word; value - list, where [0] - length of word. [1] - set of symbols
        dict_words = dict()
        for word in words:
            dict_words[word] = [len(word), set(word)]
        out = []  # final list with longest words consisting of unique symbols
        for i in range(10):
            max_length = 0
            max_uss = 0
            for word, values in dict_words.items():
                if (
                    len(values[1]) >= max_uss
                    and values[0] >= max_length
                    and word not in out
                ):
                    max_uss = len(values[1])
                    max_length = values[0]
                    cash = word
            out.append(cash)
        return out


def get_rarest_char(file_path: str) -> str:
    # Probably, there are a few of rarest symbols, this func will return one of them
    with open(file_path, encoding="unicode_escape") as f:
        text = re.sub(r"\W", "", f.read())
        d = dict()
        for i in text:
            d[i] = d.get(i, 0) + 1
        min_value = 1000
        for key, value in d.items():
            if value < min_value:
                min_value = value
                cash = key
        return cash


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        punctuation_symbols = [".", ",", "!", "?", ";", ":", "-"]
        counter = 0
        for symbol in f.read():
            if symbol in punctuation_symbols:
                counter += 1
        return counter


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode_escape") as f:
        non_ascii_symbols = [chr(i) for i in range(128)]
        counter = 0
        for symbol in f.read():
            if symbol not in non_ascii_symbols:
                counter += 1
        return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode_escape") as f:
        non_ascii_symbols = [chr(i) for i in range(128)]
        d = dict()
        for symbol in f.read():
            if symbol not in non_ascii_symbols:
                d[symbol] = d.get(symbol, 0) + 1
        max_value = 0
        for key, value in d.items():
            if value > max_value:
                max_value = value
                cash = key
        return cash
