import random
from termcolor import colored

def directions():
    print(colored('not in word', 'red'))
    print(colored('correct position', 'green'))
    print(colored('letter in wrong position', 'yellow'))


def getWords():
    word = ""
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    return words
correct = "ggggg"

def main():
    directions()
    words = getWords()
    word = random.choice(words).lower()
    tries = 1
    while True:
        guess = input("Enter a guess: ").lower()
        while(guess not in words):
            guess = input("Enter a valid guess: ").lower()
        if(guess == word):
            break
        tries += 1
        wordCopy = word
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
    print(colored(" ".join(list(word)), 'green'))
    print("Nice, you got it after {} tries.".format(tries))

if __name__ == "__main__":
    main()