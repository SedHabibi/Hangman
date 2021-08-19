from word_list import words
import random as r

def choose_word():
    word = r.choice(words)
    return word.upper()

def hangman_play(word):
    print(word)
    display_word = "_" * len(word)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 6
    print("\nLet's play Hangman!\n")
    print("The word has", len(word),"number of letters.\n")
    print(display_hangman(tries))
    print(display_word)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                letters_guessed.append(guess)
                print("You have", tries, "tries left.")
            else:
                print("Good job,", guess, "is in the word!")
                letters_guessed.append(guess)
                word_as_list = list(display_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                display_word = "".join(word_as_list)
                if "_" not in display_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                words_guessed.append(guess)
                print("You have", tries, "tries left.")
            else:
                guessed = True
                display_word = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(display_word)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    human = [  #Final state: head, torso, both arms, and both legs.
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     | |
                   -
                """,
                #Head, torso, both arms, and one leg.
                """"
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     | |
                   -
                """,
                #Head, torso, and both arms.
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                #Head, torso, and one arm.
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                #Head and torso.
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                #Head.
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                #Initial stage.
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return human[tries]


def main():
    word =  choose_word()
    hangman_play(word)

main()

def play_again():
    while True:
        encore = input("Do you want to play again? (Y/N) :").upper()
        if encore == 'Y':
            main()
        else:
            print("Thank you for playing!")
            break
play_again()