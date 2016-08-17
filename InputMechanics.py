def get_word():
    secret_word = input("Please enter secret word: ") #store input in variable

    return secret_word #return word to be guessed

def get_guess():
    single_letter=False

    while single_letter==False:
        guess=input('\n\nPlease enter your guess: ')
        if len(guess)==1:
                return guess
        print("\n\nPlease input just one letter.")
