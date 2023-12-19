# MorseCode converter
import logo
import os

with open('morse_code.txt', 'r') as file:
    morse_code = file.readlines()

# Lists for morse code
let_num_list = [code.split(' ')[0].strip() for code in morse_code]
morse_list = [code.split(' ')[1].strip() for code in morse_code]

diction = (dict(zip(let_num_list,morse_list)))



# def converter
def converter(word):
    word = word.upper()
    morse_decoder_list = [diction[letter] for letter in word]
    decoder_message = " ".join(morse_decoder_list)
    print(decoder_message)

print(logo.ASCII)
need_convert = True
while need_convert:
    word = input('Provide a word to convert: ')
    converter(word)
    if word == 'quit':
        need_convert = False
        print('Thank you for using the application')
