import random
import sys
import hangman_module
import stddraw

def hangman():
    reply="yes"


    while(reply=="yes" or reply=="y"):
        guesses_left = 8

        wrong_guesses = []
        words=[]                                        #makes a list of words from lexicon file
        file=open(sys.argv[1],'r')
        for line in file:
            for word in line.split():
                words.append(word)

        random_word=random.choice(words).lower()        #choose a random word from words list

        letters=[]
        guessed_letter=None
        letters_guessed = []
        y = len(random_word)
        if (y>=4):
            for i in random_word:
                letters.append("_") #fills up letters list containing as many number of dashes( _ ) as there are letters in the randomly chosen word.

        else:
            hangman()
        hidden_word=None

        while(guesses_left!=0 and '_' in letters):
            hidden_word = " ".join(letters)

            stddraw.setPenColor(stddraw.WHITE)
            stddraw.filledRectangle(-1, -0.8, 2, 0.5)
            hangman_module.word(hidden_word)  # printing the word

            print("The Secret Word looks like: ",hidden_word)
            print("Attempts remaining: ",guesses_left)
            print("What's your next guess? \n")

            guessed_letter = str(input()).lower()
            if guessed_letter in letters_guessed:
                print("You have already made that guess. Make a new guess")
                continue
            else:
                pass
            letters_guessed.append(guessed_letter)

            if guessed_letter in random_word:
                hangman_module.draw_hangman(guesses_left)  # drawing hangman
                hangman_module.word(hidden_word)  # printing the word
                print("Nice guess")


            for j in range(len(random_word)):
                if guessed_letter == random_word[j]:
                    letters[j]=guessed_letter


            if guessed_letter not in random_word :

                guesses_left-=1
                print("Sorry, Wrong guess!")
                wrong_guesses.append(guessed_letter)
                w = " ".join(wrong_guesses)
                print("Wrong Guesses :", w)

                hangman_module.draw_hangman(guesses_left)  # drawing hangman
                hangman_module.word(hidden_word)  # printing the word
                hangman_module.wrong_guesses(" ".join(wrong_guesses)) #Printing wrong guesses



        if "_" not in letters:
            print("Congratulations! You guessed the secret word: \n")
            print(random_word)
            stddraw.setFontSize(40)
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.text(-0.2, -0.3, "YOU WON !")
            hangman_module.correct_word(random_word) # printing the word
        else:
            print("Sorry, You lost the game. The secret word was: \n")

            print(random_word)
            stddraw.setFontSize(40)
            stddraw.setPenColor(stddraw.RED)
            stddraw.text(-0.2, -0.3, "YOU LOST")
            hangman_module.correct_word(random_word)  # printing the word

        print("Do you want to play again?\n")
        reply=str(input())

print("Welcome to CPSC-231 Console Hangman!")

hangman()
stddraw.show(0)
