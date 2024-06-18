# Write a python program that removes all punctuation from a given string

import string
def remove_punctuation(input_string):
    for char in string.punctuation:
        input_string = input_string.replace(char, '')
    return input_string


sample_text = "Hello, world! How's everything?"
cleaned_text = remove_punctuation(sample_text)
print("Original text:", sample_text)
print("Text without punctuation:", cleaned_text)
