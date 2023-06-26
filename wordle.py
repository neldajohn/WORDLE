'''
Name: Nelda
Game: NY Times Wordle

Extra:
    - Have sign in and keep score updated
    - Check if the entry for everything is either a number or a string
    - Scrape words from an online place

'''


#import
import maskpass
import base64
import random



import colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style



#global variables
game_round = 1
num_players = 0

word_length = 0
secret = ""
secretlist = ["WATER", "POLIO", "WATERY","RAINBOW"]


box_row = 1
score = 0 
word = ""
myrow = ""


p1_score = 0
p1_name = ""
p2_score = 0
p2_name = ""
final_score = "0"

play_game = 1

game_instructions = ("\t 1. First select the length of the words you will be guessing" +
      "\n \t 2. Next, let the second player enter a secret word" +
      "\n \t 3. The first player gets to guess until he/she runs out of turns" +
      "\n \t \t If the letters appear: " +
      "\n \t \t - Green: correct letter, correct position" +
      "\n \t \t - Yellow: correct letter, wrong position" +
      "\n \t \t - Red: wrong letter, wrong position" + 
      "\n \t 4. The first player then enters a secret word for the second player to guess" +
      "\n \t 5. The second player guesses until the end of his/her turn" +
      "\n \t 6. The game repeats for another round")



#initiate list of guesses
guesslist = []

###CLASSES
class player:
    #initialize player details
    def __init__(self, name = "Player", score = 0):
        self.name = str(name)
        self.score = int(score)

### declare global player values
p = player()
p1 = player()
p2 = player()

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


###FUNCTIONS

        #game instructions
def instructions(message):
    print("WELCOME TO WORDLE")
    print("\n INSTRUCTIONS: " + "\n\t")
    print(message)
        
        #decide the number of players
def numplayers():
    num_players = int(input("\nPlease select the number of players. " +
                        "\n\t Enter 1 for 1 player, 2 for two players: "))
    while (num_players != 1 and num_players != 2):
        num_players = input ("\n\t Enter 1 for 1 player, 2 for two players: ")
    

    return num_players

def game_beginning():
    #print out the game's instructions
    instructions(game_instructions)
    num_players = numplayers()
    #ask for usernames
    
    game_users = usernames(num_players)

    return num_players, game_users

        #asking for usernames
def usernames(players):
    if players == 2:
        p1_name = input ("\nPlayer 1, please enter your username: ")
        p2_name = input ("\nPlayer 2, please enter your username: ")

        return p1_name, p2_name
    else:
        p_name = input ("\nPlayer, please enter your username: ")

        return p_name

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
        secretword = input( "Please set a fitting secret word: ")

    return str(secretword)
        
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
        newrow = compare (myrow, word.upper(), secret.upper())
        guesslist[box_row] = newrow
        

    return guesslist

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

        #player guesses word
def guessing(player_name = "Player", word_length = 0):
    input_ask =  (str(player_name) + ", please enter your guess: ")

    word = input(input_ask) ###change names
    while (len(word) != word_length):
        word = input(input_ask) ###change names

    return word

        #check if the players want to exit the game
def to_continue(players_num = 0):
    values = ["Y", "X"]
    print ("\n **Wanna play another round?")
    play_game = input("\n\tEnter 'Y' or 'y' to continue or 'X' or 'x' to exit the game: ")
    while play_game.upper() not in values:
        play_game = input("\n Please enter 'Y' or 'y' to continue or 'X' or 'x' to exit the game: ")

    if (play_game.upper() == "X"):
        return False
    else:
        return True
            
        
        #the actual game
def game():

    #the beginning of the game
    if (game_round == 1):
        game_details = game_beginning()
        global num_players
        num_players = game_details[0]
        if num_players != 1:
            global p1
            global p2
            p1 = player(str(game_details[1][0]), 0)
            p2 = player(str(game_details[1][1]), 0)

        else:
            global p 
            p = player(str(game_details[1]), 0)
    else:
        pass
    
        
    #define variables
    print ("\n\t\t ***** ROUND ", str(game_round), " *****\n")
    word_length = length()
    num_guesses = word_length+1
    num_rows = num_guesses
    num_cols = word_length
    box_row = 1 
    score = 0
    turn = 1
    

    for i in range(num_players):
        #request secret word

        if (num_players == 1):
            current_player = p
            #select random word from the secret list
            index = random.randint(0, len(secretlist)-1)
            my_secret = secretlist[index]
            while (len(my_secret) != word_length):
                index = random.randint(0, len(secretlist)-1)
                my_secret = secretlist[index]
        else:
            if (turn%2 == 1):
                current_player = p1
                other_player = p2
            elif (turn%2 == 0):
                current_player = p2
                other_player = p1
            ask_input = str(current_player.name.capitalize() + ", please set a " + str(word_length) + "-letter secret word for " +
                            other_player.name.capitalize() + ": ")


            my_secret = maskpass.askpass(prompt = ask_input, mask = "*")
        
        secretword = secret(my_secret, word_length)


        #initiate list of guesses
        guesslist = []
        
        #show and print the plain display 
        guesslist = box(guesslist, box_row, num_rows, num_cols)
        for i in (guesslist):
            print(i)
            
        #set tries left
        tries_left = num_guesses

        
        #request a guess word from the player
        for i in range (num_guesses):
            #printing the tries left 
            print("\n \t Tries Left: " + str(tries_left))
            #ask the player to guess
            word =  guessing(other_player.name.capitalize(), word_length)
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
            
                #box_row += 2 #jump to the next row
                #tries_left -=1 #adjust no. of tries left
                for i in (guesslist):
                        print(i)
                score = str(len(guesslist) - box_row)
                break
        turn+=1

           

    #print the final score:
    print("\n  SCORE: " + "\n \t " + str(score))

    return to_continue(num_players)



#---------------THE MAIN GAME


    #initiate the game
while (game() == True):
    game_round += 1
    
    

print ("\n\t FINAL SCORE: " + final_score)

