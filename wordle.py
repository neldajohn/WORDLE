'''
Name: Nelda
Game: NY Times Wordle

'''


#import
import colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


#global variables
word_length = 0
secret = ""


box_row = 1
score = 0 
word = ""
myrow = ""

#initiate list of guesses
guesslist = []


#class of each letter
class letter:
    #initialize variables
    mystring = ""

    def __init__(self, alphabet, position, color = None):
        self.alphabet = alphabet
        self.position = position
        self.color = color
    
    def show(self):
        
        if (self.color == None):
            mystring ="| " + self.alphabet.upper() + " |"

        elif (self.color == "GREEN"):
            mystring ="| " + (Fore.GREEN + self.alphabet.upper() + Style.RESET_ALL) + " |"

        elif (self.color == "YELLOW"):
            mystring ="| " + (Fore.YELLOW + self.alphabet.upper() + Style.RESET_ALL) + " |"

        else:
            mystring ="| " + (Fore.RED + self.alphabet.upper() + Style.RESET_ALL) + " |"
        
        return mystring


###create functions

        #game instructions
def instructions(message):
    print("\n INSTRUCTIONS: " + "\n\t")
    print(message)

        #length of the guess words
def length():

    word_length = int(input("\n Please set the length of the words you will be guessing: "))

#---> check if word_length is number
    
    while (word_length != int(5) and word_length != int(6) and word_length!= int(7)):
        print("\n \t The game only allows 5-,6-, or 7-word guesses")
        word_length = int(input("\t Please set the length of the words you will be guessing: "))

    return word_length

        #secret word
def secret(secretword = None, word_length = 0):
    while (len(secretword) != word_length):
        secretword = input( " Player 1, please set a fitting secret word: ")

    return str(secretword)

        #compare the word and the secret
def compare(row = "", word = None, secret = None):
    myrow = row
    for i in range(len(word)):
        if word[i] in secret:
            
            if word[i] == secret[i]:
                myletter = letter(word[i], i, "GREEN")
            else:
                myletter = letter(word[i], i, "YELLOW")

        else:
            myletter = letter(word[i], i, "RED")

        myrow = myrow + str(myletter.show())

            
    return myrow
        
        #display progress
def box(guesslist = [], box_row = 1, num_rows = 0, num_cols = 0, word = None, secret = None, color = None):
    if (word == None):

        for row in range(0, 2*(num_rows)+1):
            if (row%2 == 0):
                myrow = ""
                for col in range(num_cols):
                    if (col != num_cols-1):
                        myrow = myrow + "+---+"
                    else:
                        myrow = myrow + "+---+"
                        guesslist.append(myrow)
            else:
                myrow = ""
                
                for col in range(num_cols):
                    if (col != num_cols-1):
                        myrow = myrow + "|   |"
                    else:
                        myrow = myrow + "|   |"
                        guesslist.append(myrow)
    else:
        myrow = ""
        newrow = compare (myrow, word, secret)
        guesslist[box_row] = newrow
        

    return guesslist

        #player guesses word
def guessing(word_length = 0):
    word = input( "Player 2, please enter your guess: ")
    while (len(word) != word_length):
        word = input( "Player 2, please enter your guess: ")

    return word

#welcome user
print("WELCOME TO WORDLE")

my_message = ("\t 1. First select the length of the words you will be guessing" +
      "\n \t 2. Next, let the first player enter a secret word" +
      "\n \t 3. The second player gets to guess until he/she runs out of turns" +
      "\n \t 4. Player 2 then enters a secret word for player 1 to guess" +
      "\n \t 5. Player 1 guesses until the end of their turn" +
      "\n \t 6. The game repeats for another round")


def game():
    #initiate game
    instructions(my_message)

    #define variables
    word_length = length()
    num_guesses = word_length+1
    num_rows = num_guesses
    num_cols = word_length
    box_row = 1
    

    #request secret word
    my_secret = input("\n Player 1, please set a "+ str(word_length)+"-letter secret word: ")
    secretword = secret(my_secret, word_length)

    #initiate list of guesses
    guesslist = []
    
    #show and print the plain display 
    guesslist = box(guesslist, box_row, num_rows, num_cols)
    #get input from user
    tries_left = num_guesses
    for i in (guesslist):
        print(i)

    #print("\n \t Tries Left: " + str(tries_left))


    
    #request a guess word from the player

    for i in range (num_guesses):
        print("\n \t Tries Left: " + str(tries_left))
        word =  guessing(word_length)
        if (word.upper() != secretword.upper()):
            guesslist = box(guesslist, box_row, num_rows, num_cols, word, secretword)
        
            box_row += 2 #jump to the next row
            tries_left -=1 #adjust no. of tries left
            for i in (guesslist):
                    print(i)
            #update the score
            score = str(len(guesslist) - box_row)

        else:
            guesslist = box(guesslist, box_row, num_rows, num_cols, word, secretword)
        
            box_row += 2 #jump to the next row
            tries_left -=1 #adjust no. of tries left
            for i in (guesslist):
                    print(i)
            break

       
            
        
    '''   
    word =  guessing(word_length)
    while ((word.upper() != secretword.upper()) and box_row <= (2*(num_rows+1))+1 ):
        print ("This is my box row", str (box_row))
        #box row needs to be fixed
        # print box after every guess and adjust row
        print("\n \t Tries Left: " + str(tries_left))
        
        #request a guess word from the player
        word = str (guessing(word_length))

        #adjust guesslist and display
        guesslist = box(guesslist, num_rows, num_cols, word, secretword)
        
        box_row += 2 #jump to the next row
        tries_left -=1 #adjust no. of tries left
        for i in (guesslist):
                print(i)
        #update the score
        score = str(len(guesslist) - box_row)'''

    #print the final score:
    print("\n  SCORE: " + "\n \t \t" + score)

#call the game
game()

 
