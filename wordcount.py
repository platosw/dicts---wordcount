"""Count words in file."""


# put your code here.
import sys

TEXT_FILE = open(sys.argv[1])

word_count = {}


def tokenize(filename):
    result = []
    for line in filename:
        word = line.split()
        result.extend(word)
    return result


def count_words(words):
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1


def print_word_counts(word_count):
    for key, value in word_count.items():
        print(f'{key} {value}')


def solution():
    words = tokenize(TEXT_FILE)
    count_words(words)
    print_word_counts(word_count)


solution()
