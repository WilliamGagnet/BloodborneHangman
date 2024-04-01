import random

print("Welcome to Hangman!")
keepPlaying = True

# main game loop
while(keepPlaying == True):
    # chooses the list of words the game can pull from i.e. standard version or Bloodborne version
    gameType = input("Do you want to play the Bloodborne version?(y / n) ")
    if(gameType == 'y'):
        wordsFile = open(r"C:\Users\William Gagnet\Documents\BloodborneHangmanWords.txt")
        print("Notice: The Bloodborne version has some capitalized words.")
        print("Notice: Input only one letter at a time.")
    else:
        wordsFile = open(r"C:\Users\William Gagnet\Documents\HangmanWords.txt")
        print("Notice: Input only one letter at a time.")

    # choose a random word from the selection for the game
    words = []
    for word in wordsFile:
        words.append(word.strip())
    wordsIndex = random.randint(0, len(words) - 1)
    word = words[wordsIndex]

    # make the string that will be displayed in game
    displayWord = ""
    for i in range(0, len(word)):
        displayWord += "_"

    # adds spaces to  displayWord if there are spaces in word
    if " " in word and " " not in displayWord:
        for i in range(0, len(word)):
            if " " == word[i]:
                displayWord = list(displayWord)
                displayWord[i] = " "
                displayWord = "".join(displayWord)

    # have user select how many incorrect guesses are allowed
    difficulty = int(input("How many chances do you want? "))
    guessesLeft = difficulty

    selectedLetters = ""
    numGuesses = 0
    guesses = []

    # sub game loop; continues turn until no guesses remain
    while guessesLeft != 0:
        # checks if player has won the game
        if displayWord == word:
            print()
            print(displayWord)
            print("Congrats, you win!")
            break

        # prints the status of the game
        print(displayWord)
        print("Guesses remaining: {0}".format(guessesLeft))
        print("Guessed letters: {0}".format(guesses))
        guess = input("What letter do you guess? ")

        # handles already guessed words list
        if guess not in guesses:
            guesses.append(guess)

        # handles condition of if user guesses correct letter; updates the displayed word
        if guess in word:
            numGuesses += 1
            for i in range(0, len(word)):
                if guess == word[i]:
                    displayWord = list(displayWord)
                    displayWord[i] = guess
                    displayWord = "".join(displayWord)

        # handles condition of if user guesses incorrect letter
        if guess not in word:
            guessesLeft -= 1
            numGuesses += 1

    # prints game over information
    print()
    print("Game Over")
    if(word != displayWord):
        print("The word was {0}".format(word))
    print("Number of guesses {0}".format(numGuesses))
    print("Guessed letters: {0}".format(guesses))

    # asks user if they want to play again or exit
    descision = input("Do you want to play again?(y / n) ")
    if(descision == 'n'):
        keepPlaying = False
        print("Thanks for playing!")