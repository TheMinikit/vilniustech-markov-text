import random


def replace_unnecessary_symbols(word_to_modify):
    temp_word = word_to_modify.lower()
    temp_word = temp_word.replace('.', '')
    temp_word = temp_word.replace(',', '')
    temp_word = temp_word.replace('"', '')
    temp_word = temp_word.replace("'", '')
    temp_word = temp_word.replace(':', '')
    temp_word = temp_word.replace('!', '')
    temp_word = temp_word.replace('?', '')
    temp_word = temp_word.replace('-', '')
    temp_word = temp_word.replace('\n', '')
    temp_word = temp_word.replace("--", '')
    return temp_word


ngramlength = int(input("Enter n-gram length: "))
text_length = int(input("Enter length of text to generate: "))

word_dictionary = {}

# f = open("words.txt", "r")
file_input = open("harrypotter1.txt", "r")

file_string_lines = file_input.readlines()
file_input.close()

for line in file_string_lines:

    modified_line = line.replace('\n', '')
    #  modified_line = modified_line.replace('.', ' .')
    file_string_line = modified_line.split(' ')

    for i in range(len(file_string_line)):

        current_word = replace_unnecessary_symbols(file_string_line[i])
        if len(current_word) == 0:
            continue

        prev_word = ''
        next_word = ''

        if current_word not in word_dictionary.keys() and current_word != '':
            word_dictionary[current_word] = []

        if i != len(file_string_line) - 1:
            next_word = ''
            if ngramlength > len(file_string_line) - (i + 1):
                amount_of_words = len(file_string_line) - (i + 1)
            else:
                amount_of_words = ngramlength
            for i2 in range(amount_of_words):
                if next_word == '':
                    next_word = next_word + replace_unnecessary_symbols(file_string_line[i + i2 + 1])
                else:
                    next_word = next_word + " " + replace_unnecessary_symbols(file_string_line[i + i2 + 1])
            word_dictionary[current_word].append(next_word)

#  print("Found " + str(len(word_dictionary.keys())) + " unique words")
"""
for key in word_dictionary.keys():
    print(key + " " + str(word_dictionary[key]))
"""

text_word = "harry"
markov_text = text_word

for i in range(text_length):
    word_index = random.randrange(len(word_dictionary[text_word]))
    words_to_add = word_dictionary[text_word][word_index]
    markov_text = markov_text + " " + words_to_add
    while words_to_add.split(' ')[-1] == '':
        words_to_add = words_to_add[:-1]
    if len(word_dictionary[words_to_add.split(' ')[-1]]) > 0:
        text_word = words_to_add.split(' ')[-1]

file_output = open("markovtext.txt", "w")
file_output.write(markov_text)
file_output.close()

print(markov_text)
