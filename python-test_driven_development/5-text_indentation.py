#!/usr/bin/python3
"""
This module includes one function to indent text after ., ?, :
"""


def text_indentation(text):
    """
    Print text with 2 newlines after . ? :

    Args:
        text: a string to indent

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        char = text[i]
        result += char
        if char in ".?:":
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            result += "\n\n"
            continue
        i += 1

    lines = result.split('\n')
    last_index = len(lines) - 1

    for i, line in enumerate(lines):
        line = line.strip()
        if i == last_index:
            print(line, end="")
        else:
            print(line)
