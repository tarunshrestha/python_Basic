import random

#import hangman_words

stages = ['''
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

word_list = ["aardvark", "baboon", "camel"]
#wordlist = hangmanword.words
chose_word = random.choice(word_list)


#def letter(guess):
#       return print("Right") if letter == guess else print("false")

display = []
word_length = len(chose_word)
for _ in range(word_length):
    display += "_"
    
game_over = False
lives = 6;

while not game_over :
    guess = input("Guess the word:").lower()

    for position in range(word_length):
        letter = chose_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
        
    print(f"{' '.join(display)}")
    #print(lives)
    
    if "_" not in display:
        game_over = True 
        print("Player has won" )
        
    print(stages[lives])

