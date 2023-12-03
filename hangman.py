import random

words = ["MOBILE", "LAPTOP","UMBRELLA", "SMARTWATCH"]
word = random.choice(words)

tatal_chances = 7
guessed_word = "_"*len(word)

print(guessed_word)
letter = input("Guess a letter: ").upper()
if letter in word:
    for index in range(len(word)):
        if word[index]==letter:
            guessed_word = guessed_word[:index]+letter+guessed_word_word[index+1:]
            print(guessed_word)
    if guessed_word == word:
        print("congratulations you won!")


    else:
        total_chances -= 1
        print("Inocrrect guess")
        pront("the remaining chances are: ",total_chances)
else:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")
print("the correct word is",word)
