#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Dec 2022
# This program translates anything to Pig Latin


def to_pig_latin(text):
    words = text.split()
    translated_words = []

    for word in words:
        if len(word) == 1:
            translated_word = word + "ay"
        else:
            translated_word = word[1:] + word[0] + "ay"
        translated_words.append(translated_word)
    translated_text = " ".join(translated_words)

    return translated_text


def main():
    # Gets from user
    user_input = input("Write a anything you want to translate to Pig Latin: ")
    user_input_translated = to_pig_latin(user_input)
    print("\n{}.".format(user_input_translated))

    print("\nDone.")


if __name__ == "__main__":
    main()
