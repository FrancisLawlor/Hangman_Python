import InputMechanics
import OutputUtilities
import GameMechanics

lives=6 #game starts with 6 lives
secret_word=InputMechanics.get_word() #secret_word is set initially
OutputUtilities.clear_screen()
lower_secret_word=secret_word.lower() #change secret_word to all lower case
disguised_word=GameMechanics.disguise_word(secret_word) #disguise the secret_word with underscores
guessed_letters=[] #empty list to store previously guessed letters

while GameMechanics.compare_secret_with_revealed(secret_word, disguised_word)==False: #loop will continue until secret_word and disguised_word are exactly the same i.e the underscores are replaced with letters.
    print ("\n\n")

    OutputUtilities.print_gallows(lives) #print the gallows depending on the number of lives.
    OutputUtilities.print_disguised_word(disguised_word) #print out the disguised word.

    if lives==0:
        print ("\n\nYou have no lives remaining.\n\nGAME OVER")
        input("\nThank you for playing! Push any key to exit.")
        raise SystemExit

    if len(guessed_letters)>0: #if this is not the first guess. (guessed_letters will have a length of 0 at the start).
        print ("\n\nGuessed letters: ")
        for i in range(0, len(guessed_letters)):
            print (guessed_letters[i], end=",") #print out each of the letters previously guessed, divided with commas.

    repeated_guess=True #set boolean  variable to false initially.

    while repeated_guess==True: #while letter you guess is a repeated letter (it will break when it's not a repeated letter).
        print ("\n\nYou have ", end="")
        print (lives, end="")
        print (" lives remaining.", end="")
        guess=InputMechanics.get_guess() #obtain letter for guess.
        OutputUtilities.clear_screen()
        print ("You guessed " + guess + "!\n\n" + guess + " occurs ", end="")
        print (GameMechanics.count_guess_occurrence(lower_secret_word, guess), end="")
        print (" time(s).")
        guess=guess.lower() #change guessed letter to lower case for comparison with lower case list
        repeated_guess=GameMechanics.has_been_guessed(guess, guessed_letters) #whether or not loop repeats depends on this line.

    guessed_letters.append(guess) #add the current letter to the list of previously guessed letters.

    lives=GameMechanics.update_lives(lives, secret_word, guess) #update number of lives.

    disguised_word=GameMechanics.reveal_letters(lower_secret_word,secret_word,disguised_word,guess) #reveal the necessary letters in the disguised string

    if GameMechanics.compare_secret_with_revealed(secret_word, disguised_word)==True: #if both secret_word and disguised_word are exactly the same, player wins.
        print ("\nSecret word/sentence: ", end="")
        OutputUtilities.print_disguised_word (disguised_word) #print out the disguised word.

        print ("\n\nYou win!\n\nGAME OVER")
        input("\nThank you for playing! Push enter to exit.")
