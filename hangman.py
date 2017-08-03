import InputMechanics
import OutputUtilities
import GameMechanics

lives = 6
secret_word = InputMechanics.get_word()
OutputUtilities.clear_screen()
lower_secret_word = secret_word.lower()
disguised_word = GameMechanics.disguise_word(secret_word)
guessed_letters = []

while GameMechanics.compare_secret_with_revealed(secret_word, disguised_word) == False:
    OutputUtilities.print_gallows(lives)
    OutputUtilities.print_disguised_word(disguised_word)

    if lives == 0:
        print ("\n\nYou have no lives remaining.\n\nGAME OVER")
        input("\nThank you for playing! Push any key to exit.")
        raise SystemExit

    if len(guessed_letters) > 0:
        print ("\n\nGuessed letters: ", end = '')
        for i in range(0, len(guessed_letters)):
            print (guessed_letters[i], end = ",")

    repeated_guess = True

    while repeated_guess == True:
        print ("\n\nYou have ", end = "")
        print (lives, end = "")
        print (" lives remaining.", end = "")
        guess=InputMechanics.get_guess()
        OutputUtilities.clear_screen()
        print ("You guessed " + guess + "!\n\n" + guess + " occurs ", end = "")
        print (GameMechanics.count_guess_occurrence(lower_secret_word, guess), end = "")
        print (" time(s).")
        guess = guess.lower()
        repeated_guess = GameMechanics.has_been_guessed(guess, guessed_letters)

    guessed_letters.append(guess)

    lives = GameMechanics.update_lives(lives, secret_word, guess)

    disguised_word = GameMechanics.reveal_letters(lower_secret_word, secret_word,disguised_word, guess)

    if GameMechanics.compare_secret_with_revealed(secret_word, disguised_word) == True:
        print ("\nSecret word/sentence: ", end = "")
        OutputUtilities.print_disguised_word(disguised_word)

        print ("\n\nYou win!\n\nGAME OVER")
        input("\nThank you for playing! Push enter to exit.")
