import random
  
score = 0
print("---Jumbled Word Guessing Game---")
print("All words are based on Python terms.")
player_name = input('Please enter your name: ') 

while True:
        
    words = [
    "import",
    "from",
    "as",
    "in",
    "is",
    "not",
    "and",
    "or",
    "if",
    "else",
    "elif",
    "for",
    "while",
    "break",
    "continue",
    "return",
    "yield",
    "def",
    "class",
    "pass",
    "global",
    "nonlocal",
    "del",
    "try",
    "except",
    "finally",
    "raise",
    "assert",
    "with",
    "lambda",
    "True",
    "False",
    "None",
    "print",
    "input",
    "int",
    "float",
    "str",
    "bool",
    "list",
    "tuple",
    "dict",
    "set",
    "range",
    "len",
    "max",
    "min",
    "sum",
    "sorted",
    "reversed",
    "enumerate",
    "zip",
    "map",
    "filter",
    "reduce",
    "open",
    "close",
    "read",
    "write",
    "seek",
    "tell"
] 
    pick = random.choice(words)

    random_word = random.sample(pick, len(pick)) 
    jumbled = "".join(random_word)
    print("Jumbled word is :", jumbled)

    answer = input("Try to unjumble the word. Your answer: ")
    #                                   1
#----------------------------------------------------------------
    if answer == pick:
        score += 1
        print("Your score is :", score)
#----------------------------------------------------------------
#                                   2
#----------------------------------------------------------------
        if score == 10:
            print("Congratulation ",player_name , "you win!")
            print("Your score is :", score)
            break 
#----------------------------------------------------------------
#                                   3
#----------------------------------------------------------------
    else:
        print("Game Over - The correct word is :", pick)
        print("Your score is ", score)    
        quit_score = score
        score = 0
        cont = input("press 'y' to continue and 'n' to quit : ") 
        if cont == "n":
            print(player_name, "Your score is :", quit_score)
            print("Thanks for playing...")
            break 
#-----------------------------------------------------------------
