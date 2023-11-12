import random

#word list
word_list_file = open("wordlist.txt", "r")
word_list_read = word_list_file.read()
word_list = word_list_read.split('\n')
from hangman_art import stages
from hangman_art import logo
print(logo)


#variables
random_index = random.randrange(len(word_list))
chosen_word = word_list[random_index]
word_length = len(chosen_word)
guess_no = 0
lives = 6

#hangman
display = []
for _ in range(word_length):
    display += "_"

#print(str(chosen_word))

while lives > 0:
    guess_no +=1
    if "_" in display:
        print(stages[lives])
        print(display)
        print(lives)
        guess = input("Please Guess a letter: ").lower()

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
    if '_' not in display:
        print('you won!')
        break
-
if lives > 0:
     print('Well done!')
elif lives == 0:
    print(stages[lives])
    print('you lose try again!')

