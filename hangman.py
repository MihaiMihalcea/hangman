import random

word_list = ["aardvark", "baboon", "camel", "spirited", "memory", "appliances", "trainstation"]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stage = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    \n'''

def welcome():
    print(logo)

def random_word():                                                                                                   
    global chosen_word
    chosen_word = random.choice(word_list)

def display():                                                                    
    global display
    display = [letter for letter in chosen_word]
    global remaining
    remaining = ['_' for letter in display]

def guess():                                                                      
    global guess_letter
    guess_letter = input("Please pick a letter: ").lower()
    while guess_letter not in alphabet:
        guess_letter = input("Please pick only letters: ")

def replace():
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            global remaining
            remaining[position] = letter

def guessing():
    random_word()
    display()
    letters_found = 0
    lives_left = 6
    game_on = True
    while game_on == True:
        while letters_found != len(chosen_word) and lives_left > 0:
            guess()
            replace()
            count = 0
            for letter in chosen_word:
                if letter == guess_letter:
                    letters_found += 1
                    count =+ 1
            if count > 0:    
                print("You have found a match!")
                print(f"Here's how many letters you still have to find: {' '.join(remaining)}")
                print(f"You still have {lives_left} tries left.")
            else:
                lives_left -= 1
                print(f"You haven't found any match. You have {lives_left} tries left.")
                if lives_left == 5:
                    print(stage[6])
                elif lives_left == 4:
                    print(stage[5])
                elif lives_left == 3:
                    print(stage[4])
                elif lives_left == 2:
                    print(stage[3])
                elif lives_left == 2:
                    print(stage[2])
                elif lives_left == 1:
                    print(stage[1])
        if letters_found == len(chosen_word):
            print('Congratulations, you won!')
            game_on = False
        if lives_left < 1:
            print("You have lost.")
            print(stage[0])
            game_on = False

welcome()
guessing()


