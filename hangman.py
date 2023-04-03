from string import ascii_lowercase as letters
from colorama import init, Fore
init(autoreset=True)

from proverbs import Proverbs


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
                        12 : '____\n|  |\n|  x\n| /|\\\n/\\/ \\'
                       }


    def __init__(self, sentence_to_guess):
        self.sentence_to_guess = sentence_to_guess
        self._hidden_sentence_to_guess = Hangman.mask_sentence(self.sentence_to_guess)
        self.chance = 1
        self.max_chances = len(Hangman.HANGMAN_PICTURES) - 1
        self._possible_letters = ' '.join([l for l in letters])
        self.used_letters = []
        print(Fore.CYAN + f"\nGuess the proverb: \n\n{self.hidden_sentence_to_guess} \n\nYou have 11 chances to guess the proverb")


    @property    
    def hidden_sentence_to_guess(self):
        return self._hidden_sentence_to_guess


    @hidden_sentence_to_guess.setter    
    def hidden_sentence_to_guess(self, value):
        self._hidden_sentence_to_guess = value


    @property    
    def possible_letters(self):
        return self._possible_letters


    @possible_letters.setter
    def possible_letters(self, letter):
        self._possible_letters = self._possible_letters.replace(letter, '')


    def provide_value(self):
        while True:
            print(Fore.CYAN + f"Already used letters: {' '.join(sorted(self.used_letters))}")
            print(f"Available letters: {self.possible_letters}")
            value = input("\nProvide one letter: ")
            if value in letters and len(value) == 1:
                if value not in self.used_letters:
                    self.used_letters.append(value)
                    self.possible_letters = value
                return value
            else:
                print(Fore.RED +"It's not a letter. Please provide one letter")


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
        print(Fore.CYAN + f"\n{self.hidden_sentence_to_guess}\n")
        print(Fore.YELLOW + Hangman.HANGMAN_PICTURES[self.chance])


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
                print(Fore.GREEN + f"\nCongratulations! :) That's the proverb: {self.sentence_to_guess}")
                Hangman.play_again()
                break
        else:
            print(Fore.RED + f"\nGame over! :( You've taken all your chances. That's the hidden proverb: {self.sentence_to_guess}")
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
