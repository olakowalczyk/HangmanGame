import random
from string import ascii_letters as letters
from proverbs import Proverbs
from colorama import init
init(autoreset=True)

sentences = Proverbs()
hangman = { 1 : '', 
            2 : '/', 
            3 : '/\\', 
            4 : '|\n|\n|\n/\\', 
            5 : '____\n|  \n|\n|\n/\\', 
            6 : '____\n|  |\n|\n|\n/\\', 
            7 : '____\n|  |\n|  o\n|\n/\\', 
            8 : '____\n|  |\n|  o\n|  |\n/\\',
            9 : '____\n|  |\n|  o\n| /|\n/\\', 
            10 : '____\n|  |\n|  o\n| /|\\\n/\\', 
            11 : '____\n|  |\n|  o\n| /|\\\n/\\/', 
            12 : '____\n|  |\n|  o\n| /|\\\n/\\/ \\'
          }
colors = {'orange' : '\033[33m',
          'green' : '\033[32m',
          'red' : '\033[31m' ,
          'purple' : '\033[35m}', 
          'blue' : '\33[36m'}


def main():
    sentence_to_guess = sentence()
    hidden_sentence_to_guess = mask_sentence(sentence_to_guess)
    print(colors['blue'] + f"\nGuess the proverb: {hidden_sentence_to_guess} \nYou have 11 chances to guess the proverb")
    chance = 1
    max_chances = 11

    while chance <= max_chances:
        print(f"\n===== Remaining chances: {max_chances - chance + 1} =====")
        letter = provide_value()
        hidden_sentence_to_guess = replace_with_letter(letter, sentence_to_guess, hidden_sentence_to_guess)
        print(colors['blue'] + f"\n{hidden_sentence_to_guess}\n")

        chance = chance if letter in sentence_to_guess else chance + 1
        print(colors['orange'] + hangman[chance])

        if hidden_sentence_to_guess == sentence_to_guess:
            print(colors['green'] + f"\nCongratulations! :) That's the proverb: {sentence_to_guess}")
            key = input("Play again? (y) ")
            if key == 'y':
                main()
            else:
                print("Thanks for playing")
                break
    else:
        print(colors['red'] + f"\nGame over! :( You've taken all your chances. That's the hidden proverb: {sentence_to_guess}")
        key = input("Play again? (y) ")
        if key == 'y':
            main()
        else:
            print("Thanks for playing")



def replace_with_letter(letter, sentence, hidden_sentence):
    """ 
        replace mask "_" with letter when letter match sentence letter
    """
    sentence = list(sentence)
    hidden_sentence = list(hidden_sentence)

    for idx, l in enumerate(sentence):
        if l == letter:
            hidden_sentence[idx] = letter
        elif l == letter.capitalize():
            hidden_sentence[idx] = letter.capitalize()
    return ''.join(hidden_sentence)


def provide_value():
    while True:
        value = input("\nProvide one letter: ")
        if value in letters and len(value) == 1:
            return value
        else:
            print("It's not a letter. Please provide one letter")


def sentence():
    return random.choice(sentences)


def mask_sentence(sentence):
    for l in sentence:
        if l.isalpha():
            sentence = sentence.replace(l, '_')
    return sentence


main()
