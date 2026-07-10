import random

# List of words
Fruits = ["Apple","Mango","Banana","Pear","Grape"]
Fruit = random.choice(Fruits)

#create a list of underscores
hidden_Fruit = []

for letter in Fruit:
    hidden_Fruit.append(" _")

# Randomly choose a word
print("Welcome to Hangman")
print("".join(hidden_Fruit))
