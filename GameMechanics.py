
def disguise_word(secret_word):
    str = [] #initialise empty list
    for i in range(0, len(secret_word)): #go through all letters
        if secret_word[i] != ' ': #if character is not a space
            str.append('_') #append underscore to list "str"
        else:
            str.append(' ') #append a space if the character in the secret_word is a space

    return str

def check_guess(secret_word_letter, guess):
    if secret_word_letter == guess: #if the letter from the word to be guessed is equal to the character the user enters to guess.
        return True
    else:
        return False

def reveal_letters(lower_secret_word, secret_word, disguised_word, guess):
    for i in range(0, len(secret_word)):
        if check_guess(lower_secret_word[i], guess): #if the lower case version of the word/sentence to be guessed is equal to the letter guessed.
            disguised_word[i] = secret_word[i] #assign the letter in the same position as the current lowercase character, in the initial sentence to be guessed, to the same position in the disguised list.

    return disguised_word

def count_guess_occurrence(lower_secret_word, guess):
    occurrences = 0 #initially there are 0 occurrences of the letter.
    for i in range(0, len(lower_secret_word)):
        if check_guess(lower_secret_word[i], guess): #each time the guessed letter occurs in the lower case list, increment the occurrences variable by 1.
            occurrences += 1

    return occurrences

def compare_secret_with_revealed(secret_word, disguised_word):
    for i in range(0, len(secret_word)):
        if secret_word[i] != disguised_word[i]:
            return False

    return True

def update_lives(lives, secret_word, guess):
    present = False
    for i in range(0, len(secret_word)):
        if check_guess(secret_word[i], guess) == True:
            present = True

    if present == False:
        lives -= 1

    return lives

def has_been_guessed(guess, guessed_letters):
    for i in range(0, len(guessed_letters)):
        if guess == guessed_letters[i]:
            print ("\nYou've guessed that before!\n\nPlease guess again.")
            return True

    return False
