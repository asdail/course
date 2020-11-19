from random import randint
from functions.indexfunctions import *
wordbank=["jonas","mashiach","oz","yoav","yonatan"]
word=wordbank[randint(0,len(wordbank)-1)]
ui="*"*len(word)
strikes=10
guesses=0
guessed_letters=[]
print(ui)
while strikes!=0 and ui!=word:
    guess=input("Guess a letter.. ")
    guessed_letters+=guess
    guesses+=1
    if guess in word:
        x=str_indexnum(word,guess)
        ui=letter_replace(ui,guess,x)
        print("Correct!")
        print(ui)
        print(guessed_letters)
    else:
        strikes-=1
        print(f"Wrong answer!\nYou have {strikes} strikes left.")
        print(guessed_letters)
else:
    if strikes==0:
        print(f"You loose. Shame.\nThe word was {word}.\nIt took you {guesses}Guesses to guess the word.")
    if ui==word:
        print(f"Congratulations! You won!\nThe word was {word}.\nIt took you {guesses} Guesses to guess the word.")
exit=input("Press sapce to exit.. ")
if exit=="":
    print("Bye Bye!")