import os
import random 
try:
  from english_words import english_words_set
except ModuleNotFoundError:
  print ("Trying to Install required module: requests\n")
  os.system('pip install english-words')
# -- above lines try to install requests module if not present
else:
    from english_words import english_words_set

def start_game(nax_tries):
    """
    This function print the logo of the game and ask for file path and index to choose a word from the file given
    :param nax_tries  : maximun tries of wrong guess represent by str
    :type nax_tries : str 
    :return : file path and index  of word 
    :rtype : str,int 
    """
    print(""" _    _\n| |  | |\n| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n| |  | | (_| | | | | (_| | | | | | | (_| | | | |
    \r|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n\t\t     __/ |\n\t\t    |___/\n""")
    print(nax_tries)
    print("\n\n\n\n\n\n")
    words_list= list(english_words_set)  
    random_index= a=random.randrange(0, len(english_words_set))
    return words_list[random_index]

def print_hangman(num_of_tries):
    """
    print Graphic illustration of failed attempts by the user so far
    :param num_of_tries  :Representing the number of failed attempts by the user so far
    :type name num_of_tries:int
    :return : Graphic illustration Representing the number of failed attempts by the user so far
    """
    HANGMAN_PHOTOS={}
    HANGMAN_PHOTOS[0]='x-------x'
    HANGMAN_PHOTOS[1]= ":(\nx-------x\n|\n|\n|\n|\n|\n"
    HANGMAN_PHOTOS[2]=":(\nx-------x\n|       |\n|       0\n|\n|\n|\n"
     
    HANGMAN_PHOTOS[3]=":(\nx-------x\n|       |\n|       0\n|       |\n|\n|\n"
    HANGMAN_PHOTOS[4]=":(\nx-------x\n|       |\n|       0\n|      /|\ \n|\n|\n"
    HANGMAN_PHOTOS[5]=":(\nx-------x\n|       |\n|       0\n|      /|\ \n|      /\n|"
    HANGMAN_PHOTOS[6]=":(\nx-------x\n|       |\n|       0\n|      /|\ \n|      / \ \n|"
    print(HANGMAN_PHOTOS[num_of_tries])
    
def check_win(secret_word, old_letters_guessed):
    """
    check if user won 
    :param secret_word  : the secret word user should guess  
    :type secret_word : str
    :param old_letters_guessed : list of letters user guess
    :type old_letters_guessed : list
    :return : true is user won
    :rtype : bool
    """
    win=True
    string=""
    for letter in secret_word:
        if letter in  old_letters_guessed:
            pass
        else:
             win=False
    return win 

def show_hidden_word(secret_word, old_letters_guessed):
    """
    show under line Represent letter from the secret word ,if user gues the letter the letter apear in place of the under line 
    :param secret_word  : the secret word user should guess  
    :type secret_word : str
    :param old_letters_guessed : list of letters user guess
    :type old_letters_guessed : list
    :return : return string with underlines and reviles letters the user guessed correct
    :rtype : str
    """
    string=""
    for letter in secret_word:
        if letter in  old_letters_guessed:
            string+=letter+' '
        else:
             string+='_ '
    return string  
    
def isEnglish(s):
    """check if letter given is english char
    :param s : letter given 
    :type s : str
    :return : true if letter is english char 
    :rtype : bool
    """
    english="abcdefghijklmnopqrstuvwxyz"
    if s in english:
        return True
    else:
        return False
        
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    check if user input  valid letter 
    :param letter_guessed : letter user guess 
    :type letter_guessed : str
    :param old_letters_guessed : list of letters user guess
    :type old_letters_guessed : list
    :return : true if letter is valid
    :rtype : bool
    """
    letter_guessed=letter_guessed.lower()
    is_valid_input=False
    letter_given_before = letter_guessed in old_letters_guessed
    is_English=isEnglish(letter_guessed)
    if(len(letter_guessed)==1 and is_English and not(letter_given_before)):
        is_valid_input=True
        
    return is_valid_input

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the function add the letter to the old_letters_guessed if is valid letter if not print 'X' and the letter the user guess so far
    :param letter_guessed : letter user guess 
    :type letter_guessed : str
    :param old_letters_guessed : list of letters user guess
    :type old_letters_guessed : list
    :return : true if letter successfully added to list of old_letters_guessed false if not
    :rtype : bool

    """
    old_letters_guessed.sort()
    letter_successfully_added=False
    
    if(check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        letter_successfully_added=True
        return letter_successfully_added
    else:
        print("X")
        s = " -> "
        print(s.join(old_letters_guessed))
        return False
        


    
def Guess_a_letter():
    """ ask from user to geuss letter
    :return : the input from user 
    :rtype : str
    """ 
    Guess_a_letter=input("Guess a letter : ")
    return Guess_a_letter


def first_print_pattern(secret_word):
    """
    the first time the game run print the starting position-  started with a string of under lines along the length of the word that should be guessed
    :param secret_word : the secret word user shoul guess 
    :type secret_word : str 
    :return : none 
    :rtype : none
    """
    print("\n\nLet’s start!")
    print_hangman(0)
    print("_ "*len(secret_word)+"\n\n")    
    
def main():

    MAX_TRIES = 6
    old_letters_guessed=[]
    secret_word=start_game(MAX_TRIES)
    first_print_pattern(secret_word)
    num_of_tries=1;
    win=False
    while num_of_tries <= MAX_TRIES and not win:
        letter=Guess_a_letter()
        letter_is_valid=try_update_letter_guessed(letter, old_letters_guessed)       
        if  letter_is_valid:
            if letter not in secret_word :
                print_hangman(num_of_tries)
                num_of_tries+=1
            print(show_hidden_word(secret_word, old_letters_guessed)+"\n\n") 
            win=check_win(secret_word, old_letters_guessed)              
                
    if win:
        print("WON")
    else:
        print("LOSE")
        print("\nthe secret word was -> " + '{}'.format(secret_word))
        
        
    do_not_close_window=input("")    
        
    
    
if __name__ == '__main__':
    main()
    