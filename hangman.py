def get_word():
    secret_word = input("Please enter secret word: ") #store input in variable

    return secret_word; #return word to be guessed

def disguise_word(secret_word):
    str=[]; #initialise empty list
    for i in range(0,len(secret_word)): #go through all letters
        if secret_word[i] != ' ': #if character is not a space
            str.append('_'); #append underscore to list "str"
        else:
            str.append(' '); #append a space if the character in the secret_word is a space

    return str;

def print_disguised_word(disguised_word):
    print ("\n");
    for i in range(0,len(disguised_word)): #loop through entire list and print every character.
        print (disguised_word[i], end=' '); #end=' ' keeps everything on one line

def check_guess(secret_word_letter, guess):
    if secret_word_letter==guess: #if the letter from the word to be guessed is equal to the character the user enters to guess.
        return True;
    else:
        return False;

def reveal_letters(lower_secret_word,secret_word, disguised_word, guess):
    for i in range(0,len(secret_word)):
        if check_guess(lower_secret_word[i],guess): #if the lower case version of the word/sentence to be guessed is equal to the letter guessed.
            disguised_word[i]=secret_word[i]; #assign the letter in the same position as the current lowercase character, in the initial sentence to be guessed, to the same position in the disguised list.

    return disguised_word;

def count_guess_occurrence(lower_secret_word, guess):
    occurrences=0; #initially there are 0 occurrences of the letter.
    for i in range(0,len(lower_secret_word)):
        if check_guess(lower_secret_word[i],guess): #each time the guessed letter occurs in the lower case list, increment the occurrences variable by 1.
            occurrences+=1;

    return occurrences;

def compare_secret_with_revealed(secret_word, disguised_word):
    for i in range(0,len(secret_word)):
        if secret_word[i]!=disguised_word[i]: #if any elements in the same positions in both lists are different, return false.
            return False;

    return True;

def clear_screen():
    for i in range(0,100): #print lots of line breaks to create the illusion of a cleared screen.
        print("\n");

def print_gallows(lives): #depending on number of lives print a different image of the stick man.
    if(lives==6):
        print ("+--------\n|\t|\n|\n|\n|\n+--------");
    if(lives==5):
        print ("+--------\n|\t|\n|\to\n|\n|\n+--------");
    if(lives==4):
        print ("+--------\n|\t|\n|\to\n|\t|\n|\n+--------");
    if(lives==3):
        print ("+--------\n|\t|\n|\to\n|      /|\n|\n+--------");
    if(lives==2):
        print ("+--------\n|\t|\n|\to\n|      /|\\\n|\n+--------");
    if(lives==1):
        print ("+--------\n|\t|\n|\to\n|      /|\\\n|      /\n+--------");
    if(lives==0):
        print ("+--------\n|\t|\n|\to\n|      /|\\\n|      / \\\n+--------");

def update_lives(lives, secret_word, guess):
    present = False; #boolean variable which corresponds to whether or not the guessed letter is in the secret_word

    for i in range(0, len(secret_word)):
        if check_guess(secret_word[i], guess)==True: #if guessed letter is equal to any element in the secret_word, then it's present
            present=True;

    if present==False:
        lives-=1; #if letter is not present, decrease number of lives by 1.

    return lives;

def has_been_guessed(guess, guessed_letters):
    for i in range(0, len(guessed_letters)):
        if guess==guessed_letters[i]: #if guessed letter is in list containing previously guessed letters:
            print ("\nYou've guessed that before!\n\nPlease guess again.")
            return True;

    return False;

def get_guess():
    single_letter=False;

    while single_letter==False:
        guess=input('\n\nPlease enter your guess: ');
        if len(guess)==1:
                return guess;
        print("\n\nPlease input just one letter.")


lives=6; #game starts with 6 lives
secret_word=get_word(); #secret_word is set initially
clear_screen();
lower_secret_word=secret_word.lower(); #change secret_word to all lower case
disguised_word=disguise_word(secret_word); #disguise the secret_word with underscores
guessed_letters=[]; #empty list to store previously guessed letters

while compare_secret_with_revealed(secret_word, disguised_word)==False: #loop will continue until secret_word and disguised_word are exactly the same i.e the underscores are replaced with letters.
    print ("\n\n");

    print_gallows(lives); #print the gallows depending on the number of lives.
    print_disguised_word (disguised_word); #print out the disguised word.

    if lives==0:
        print ("\n\nYou have no lives remaining.\n\nGAME OVER");
        input("\nThank you for playing! Push enter to exit.");
        raise SystemExit;

    if len(guessed_letters)>0: #if this is not the first guess. (guessed_letters will have a length of 0 at the start).
        print ("\n\nGuessed letters: ");
        for i in range(0, len(guessed_letters)):
            print (guessed_letters[i], end=","); #print out each of the letters previously guessed, divided with commas.

    repeated_guess=True; #set boolean  variable to false initially.

    while repeated_guess==True: #while letter you guess is a repeated letter (it will break when it's not a repeated letter).
        print ("\n\nYou have ", end="");
        print (lives, end="");
        print (" lives remaining.", end="");
        guess=get_guess(); #obtain letter for guess.
        clear_screen();
        print ("You guessed " + guess + "!\n\n" + guess + " occurs ", end="");
        print (count_guess_occurrence(lower_secret_word, guess), end="");
        print (" time(s).");
        guess=guess.lower(); #change guessed letter to lower case for comparison with lower case list
        repeated_guess=has_been_guessed(guess, guessed_letters); #whether or not loop repeats depends on this line.

    guessed_letters.append(guess); #add the current letter to the list of previously guessed letters.

    lives=update_lives(lives, secret_word, guess); #update number of lives.

    disguised_word=reveal_letters(lower_secret_word,secret_word,disguised_word,guess); #reveal the necessary letters in the disguised string

    if compare_secret_with_revealed(secret_word, disguised_word)==True: #if both secret_word and disguised_word are exactly the same, player wins.
        print ("\nSecret word/sentence: ", end="");
        print_disguised_word (disguised_word); #print out the disguised word.

        print ("\n\nYou win!\n\nGAME OVER");
        input("\nThank you for playing! Push enter to exit.");
