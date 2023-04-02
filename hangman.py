from string import ascii_letters as letters
from proverbs import Proverbs
from colorama import init
init(autoreset=True)

colors = {'orange' : '\033[33m',
        'green' : '\033[32m',
        'red' : '\033[31m' ,
        'purple' : '\033[35m}', 
        'blue' : '\33[36m'}


class Hangman:


    HANGMAN_PICTURES = { 1 : '', 
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


    def __init__(self, sentence_to_guess):
        self._sentence_to_guess = sentence_to_guess
        self._hidden_sentence_to_guess = Hangman.mask_sentence(self.sentence_to_guess)
        self.chance = 1
        self.max_chances = len(Hangman.HANGMAN_PICTURES) - 1
        self.used_letters = []
        print(colors['blue'] + f"\nGuess the proverb: {self.hidden_sentence_to_guess} \nYou have 11 chances to guess the proverb")


    @property    
    def sentence_to_guess(self):
        return self._sentence_to_guess


    @property    
    def hidden_sentence_to_guess(self):
        return self._hidden_sentence_to_guess


    @hidden_sentence_to_guess.setter    
    def hidden_sentence_to_guess(self, value):
        if isinstance(value, str):
            self._hidden_sentence_to_guess = value
        else:
            raise ValueError(f"Value is {type(value)} but it should be string")


    def provide_value(self):
        while True:
            print(colors['blue'] + f"Already used letters: {' '.join(sorted(self.used_letters))}")
            value = input("\nProvide one letter: ")
            if value in letters and len(value) == 1:
                if value not in self.used_letters:
                    self.used_letters.append(value)
                return value
            else:
                print(colors['red'] +"It's not a letter. Please provide one letter")


    def replace_with_letter(self, letter):
        sentence = list(self.sentence_to_guess)
        hidden_sentence = list(self.hidden_sentence_to_guess)

        for idx, l in enumerate(sentence):
            if l == letter:
                hidden_sentence[idx] = letter
            elif l == letter.capitalize():
                hidden_sentence[idx] = letter.capitalize()
        self.hidden_sentence_to_guess = ''.join(hidden_sentence)
        self.chance = self.chance if letter in self.sentence_to_guess else self.chance + 1
        print(colors['blue'] + f"\n{self.hidden_sentence_to_guess}\n")
        print(colors['orange'] + Hangman.HANGMAN_PICTURES[self.chance])


    @staticmethod
    def mask_sentence(sentence):
        for l in sentence:
            if l.isalpha():
                sentence = sentence.replace(l, '_')
        return sentence


    def play(self):
        while self.chance <= self.max_chances:
            print(f"\n{'-'*20}  Remaining chances: {self.max_chances - self.chance + 1} {'-'*20}")
            letter = self.provide_value()
            self.replace_with_letter(letter)

            if self.hidden_sentence_to_guess == self.sentence_to_guess:
                print(colors['green'] + f"\nCongratulations! :) That's the proverb: {self.sentence_to_guess}")
                Hangman.play_again()
                break
        else:
            print(colors['red'] + f"\nGame over! :( You've taken all your chances. That's the hidden proverb: {self.sentence_to_guess}")
            Hangman.play_again()


    @staticmethod
    def play_again():
        key = input("Play again? (y) ")
        if key == 'y':
            hangman = Hangman((proverbs.get_random_proverb()))
            hangman.play()
        else:
            print("Thanks for playing")


if __name__ == "__main__":
    proverbs = Proverbs()
    hangman = Hangman(proverbs.get_random_proverb())
    hangman.play()
