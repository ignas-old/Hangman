def hangman(word):
    
    wrong_guesses = 0
    letter_display = "_"*len(word)
    max_wrong_guesses = 5

    print(r"""   _____
   |    |
   |    O
   |   /|\
   |   / \
 __|__""")
    print("Let's PLAY HANGMAN. Try to guess the word!")

    #guesses = ''
    current_guess = ''
    
    while wrong_guesses < max_wrong_guesses:

        for i in range(len(word)):
                if current_guess == word[i]:
                    letter_display = letter_display[:i] + current_guess + letter_display[i+1:]
        
        print(letter_display)
        current_guess = input("Guess a letter: ")

        if current_guess not in word:
            wrong_guesses += 1
            print(f"Wrong! No letter {current_guess} in my word.")
            print(f"You have {max_wrong_guesses - wrong_guesses} guesses left")
        else:
            print("Correct!")
            print(f"You have {max_wrong_guesses - wrong_guesses} guesses left")

        if "_" not in letter_display:
            print("Well done!")
            break

    if "_" in letter_display :        
        print("You Lose!")


#This method may be used later for more input logic paths

# def check_and_get_guess(previous_guesses):
    
#     guess = input("Guess a letter: ")

#     if guess in previous_guesses:
#         print("You can make a guess with only one letter")



hangman("Fucking")