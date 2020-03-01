import random
from getproverbs import get_proverbs
from colorama import init
init(autoreset=True)

sentences= get_proverbs()
#sentences=['abc']
hangman ={1: '', 2: '/', 3: '/\\', 4: '|\n|\n|\n/\\', 5: '____\n|  \n|\n|\n/\\', 6: '____\n|  |\n|\n|\n/\\', 7: '____\n|  |\n|  o\n|\n/\\', 8: '____\n|  |\n|  o\n|  |\n/\\', 9: '____\n|  |\n|  o\n| /|\n/\\', 10: '____\n|  |\n|  o\n| /|\\\n/\\', 11: '____\n|  |\n|  o\n| /|\\\n/\\/', 12: '____\n|  |\n|  o\n| /|\\\n/\\/ \\'}

def main():
    sentenceToGuess = sentence() # get random sentence
    sentenceToGuessMask = mask_sentence(sentenceToGuess) # hides the sentence to the player
    print("\nGuess the proverb: " + sentenceToGuessMask + "\nYou have 11 chances")
    chance = 1
    
    while chance <= 11: # check the letter till chances are available
        print("\n===== Chance " + str(chance) + " =====")
        letter = provide_value("\nProvide one letter: ")
        sentenceToGuessMask = replace_with_letter(letter, sentenceToGuess, sentenceToGuessMask)
        sentenceToGuessMask =''.join(sentenceToGuessMask)
        print("\n" + str(sentenceToGuessMask) + "\n")
        
        if letter in sentenceToGuess and len(letter)==1: # chance do not increment where letter match
            chance = chance
        else:
            chance = chance+1 
        print('\033[33m' + hangman[chance]) # print hangman appropiate to chance
        
        if str(sentenceToGuessMask) == sentenceToGuess:
            print('\033[32m'+"\nYOU WIN :)")
            print("\nPlay again? (y)")
            key=input()
            if key=='y':
                main()
            break
             
    else:
        print('\033[31m'+"\nGAME OVER :( \nProverb: " + str(sentenceToGuess))        
        print("\nPlay again? (y)")
        key=input()
        if key=='y':
            main()
            
def replace_with_letter(letter, sentence, sentenceMask): #replace mask ____ with letter when letter match sentence letter
    sentence = list(sentence)
    sentenceMask = list(sentenceMask)
    index_l=-1
    
    for l in sentence:
        index_l=index_l + 1
        if l == letter:
            sentenceMask[index_l]=letter
        if l == letter.capitalize():
           sentenceMask[index_l]=letter.capitalize()
    return sentenceMask
          

def provide_value(desc): #provides letter
    value = input(desc)
    return value

def sentence(): # draws sentence
    sentence = random.choice(sentences)
    return sentence

def mask_sentence(sentence): # provides masked sentence
    for l in sentence:
        if l != ' ' and l != "’" and l != ',' and l != '\'':
            sentence = sentence.replace(l, '_')
    return sentence
    

main()


