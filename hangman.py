import os
from string import ascii_lowercase as letters
from colorama import init, Fore
init(autoreset=True)

from proverbs import Proverbs


class Hangman:


    HANGMAN_PICTURES = { 0 : '\n' * 4, 
                         1 : '\n\n\n\n/', 
                         2 : '\n\n\n\n/\\', 
                         3 : '\n|\n|\n|\n/\\', 
                         4 : '____\n|  \n|\n|\n/\\', 
                         5 : '____\n|  |\n|\n|\n/\\', 
                         6 : '____\n|  |\n|  o\n|\n/\\', 
                         7 : '____\n|  |\n|  o\n|  |\n/\\',
                         8 : '____\n|  |\n|  o\n| /|\n/\\', 
                         9 : '____\n|  |\n|  o\n| /|\\\n/\\', 
                        10 : '____\n|  |\n|  o\n| /|\\\n/\\/', 
                        11 : '____\n|  |\n|  x\n| /|\\\n/\\/ \\'
                       }


    def __init__(self, sentence_to_guess):
        self.sentence_to_guess = sentence_to_guess
        self.hidden_sentence_to_guess = Hangman.mask_sentence(self.sentence_to_guess)
        self.used_chances = 0
        self.max_chances = len(Hangman.HANGMAN_PICTURES) - 1
        self.possible_letters = ' '.join([l for l in letters])
        self.used_letters = []
        self.current_picture = Hangman.HANGMAN_PICTURES[self.used_chances]
        print(Fore.CYAN + f"\nGuess the proverb: \n\n{self.hidden_sentence_to_guess} \n\nYou have 11 chances to guess the proverb")


    def provide_value(self):
        while True:
            value = input("\nProvide one letter: ")
            if value in letters and len(value) == 1:
                if value not in self.used_letters:
                    self.used_letters.append(value)
                    self.possible_letters = self.possible_letters.replace(value, ' ')
                return value
            else:
                print(Fore.RED + "It's not a letter. Please provide one letter")


    def replace_with_letter(self, letter):
        sentence = list(self.sentence_to_guess)
        hidden_sentence = list(self.hidden_sentence_to_guess)

        for idx, l in enumerate(sentence):
            if l == letter:
                hidden_sentence[idx] = letter
            elif l == letter.capitalize():
                hidden_sentence[idx] = letter.capitalize()
        self.hidden_sentence_to_guess = ''.join(hidden_sentence)
        self.used_chances = self.used_chances if letter in self.sentence_to_guess else self.used_chances + 1
        self.current_picture = self.HANGMAN_PICTURES[self.used_chances]
        

    @staticmethod
    def mask_sentence(sentence):
        for l in sentence:
            if l.isalpha():
                sentence = sentence.replace(l, '_')
        return sentence


    def display_current_status(self):
        Hangman.clear()
        print(f"\n{'-'*20}  Remaining chances: {self.max_chances - self.used_chances} {'-'*20}")
        print(Fore.CYAN + f"\n{self.hidden_sentence_to_guess}\n")
        print(Fore.YELLOW + self.current_picture)
        print(Fore.CYAN + f"Already used letters: {' '.join(sorted(self.used_letters))}")
        print(f"Available letters: {self.possible_letters}")


    def play(self):
        while self.used_chances < self.max_chances:
            self.display_current_status()
            letter = self.provide_value()
            self.replace_with_letter(letter)

            if self.hidden_sentence_to_guess == self.sentence_to_guess:
                print(Fore.GREEN + f"\nCongratulations! :) That's the proverb: {self.sentence_to_guess}")
                Hangman.play_again()
                break
        else:
            self.display_current_status()
            print(Fore.RED + f"\nGame over! :( You've taken all your chances. That's the hidden proverb: {self.sentence_to_guess}")
            Hangman.play_again()


    @staticmethod
    def play_again():
        key = input("Play again? (y) ")
        if key == 'y':
            Hangman.clear()
            hangman = Hangman((proverbs.get_random_proverb()))
            hangman.play()
        else:
            print("Thanks for playing")


    @staticmethod
    def clear():
        os.system('cls')


if __name__ == "__main__":
    proverbs = Proverbs()
    hangman = Hangman(proverbs.get_random_proverb())
    hangman.play()
