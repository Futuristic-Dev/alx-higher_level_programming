#!/usr/bin/python3

def common_elements(set_i, set_2):
    commonWords = set()
    for words in set_1:
        if words in set_2:
            commonWords.add(words)
    return commonWords
