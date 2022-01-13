import random
from termcolor import colored
print(colored('not in word', 'red'))
print(colored('correct position', 'green'))
print(colored('letter in wrong position', 'yellow'))
correct = "ggggg"
word = ""
with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    # print random string
    word = random.choice(words).upper()
i = 1
while True:
    guess = input("Enter guess: ").upper()
    if(guess == word):
        break
    i += 1
    wordCopy = word
    print(wordCopy)
    while(len(guess) != 5):
        guess = input("Enter guess: ").upper()

    colors = ""
    for i, n in enumerate(guess):
        color = "red"
        index = wordCopy.find(n)
        if(index != -1):
            color = "yellow"
            if(i == index):
                color = "green"
            wordCopy = wordCopy.replace(n, ' ', 1)
        colors += colored(n, color) + " "
        
    print(colors)
print("Noice, you got it after {} tries.".format(i))