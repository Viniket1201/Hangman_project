import string
from words import choose_word
from images import IMAGES






'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly)
      return False (wrong selection)
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
        continue
    return True

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i,'')
    return letters_left


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
                str(len(secret_word))), end='\n\n')
    letters_guessed = []
    lifeofman=8
    hint=1
    #print(secret_word)
    while True:
        if lifeofman>0:
            print("****you have",lifeofman,"lifes left.****")
            print(IMAGES[8-lifeofman])
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters))
            print("you have guessed....",get_guessed_word(secret_word,letters_guessed))
            if hint==1:
                t=input("do you want hint.....type hint.")
                if t.lower()=="hint":
                    hint-=1
                    for i in available_letters:
                        if i in secret_word:
                            letters_guessed.append(i)
                            break
                    continue
            guess = input("Please guess a letter: ")
            letter = guess.lower()

            if letter in secret_word:
                letters_guessed.append(letter)
                #print(letters_guessed)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print(" * * Congratulations, you won! * * ", end='\n\n')
                    break
            else:
                if letter not in available_letters:
                    print("Invalid Input,choose again.")
                    continue
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                letters_guessed.append(letter)
                lifeofman-=1
                print("")
        else:
            print(IMAGES[-1])
            print("Hey Pal! you have losed and the man have hang.")
            break


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)```
