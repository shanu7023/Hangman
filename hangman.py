import random
from os import clear
from hangman_words import word_list
chosen_word=random.choice(word_list)
lives=5
from hangman_art import logo,stages
print(logo)
display=[]
for letter in chosen_word:
    display+="_"
end_of_game=False
while not end_of_game:
    guess=input("guess a letter:").lower()
    if guess in display:
        print(f"you've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"you guessed {guess},that's not in the word.you lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("you win")
    print(stages[lives])


