#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    sentences = text.splitlines()

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            for char in characters:
                if char in sentence:
                    parts = sentence.split(char)
                    indented_line = '\n\n'.join([part.strip() for part in parts])
                    print(indented_line)
                    break
            else:
                print(sentence, end='')
