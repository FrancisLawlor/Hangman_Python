def print_disguised_word(disguised_word):
    print ("\n")
    for i in range(0,len(disguised_word)): #loop through entire list and print every character.
        print (disguised_word[i], end=' ') #end=' ' keeps everything on one line
        
def print_gallows(lives): #depending on number of lives print a different image of the stick man.
    if(lives==6):
        print ("+--------\n|\t|\n|\n|\n|\n+--------")
    if(lives==5):
        print ("+--------\n|\t|\n|\to\n|\n|\n+--------")
    if(lives==4):
        print ("+--------\n|\t|\n|\to\n|\t|\n|\n+--------")
    if(lives==3):
        print ("+--------\n|\t|\n|\to\n|      /|\n|\n+--------")
    if(lives==2):
        print ("+--------\n|\t|\n|\to\n|      /|\\\n|\n+--------")
    if(lives==1):
        print ("+--------\n|\t|\n|\to\n|      /|\\\n|      /\n+--------")
    if(lives==0):
        print ("+--------\n|\t|\n|\to\n|      /|\\\n|      / \\\n+--------")

def clear_screen():
    for i in range(0,100): #print lots of line breaks to create the illusion of a cleared screen.
        print("\n")
