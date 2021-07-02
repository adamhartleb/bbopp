import random

def blurb():
    print("Bagels, a deductive logic game.")
    print("")
    print("I am thinking of a 3-digit number. Try to guess what it is.")
    print("")
    print("Here are some clues:")
    print("When I say:      That means:")
    print("Pico             One digit is correct but in the wrong position.")
    print("Fermi            One digit is correct and in the right position.")
    print("Bagels           No digit is correct")

    print("")
    print("I have thought up a number. You have 10 guesses to get it.")


def get_secret_num():
    return list(str(random.randint(100, 999)))

def get_clues(guess, secret_num):
    clues = []
    for index, digit in enumerate(list(guess)):
        if digit == secret_num[index]:
            clues.append("Fermi")
        elif digit in secret_num:
            clues.append("Pico")
    return clues

def main():
    blurb()

    secret_num = get_secret_num()

    guess_count = 1
    while guess_count <= 10:
        guess = input(f"Guess #{guess_count}: ")
        if (guess == secret_num):
            print("Congratulations, you guessed the number!")
            return

        clues = get_clues(guess, secret_num)
            
        if len(clues) == 0:
            print("Bagels")
        else:
            print(" ".join(clues))
        
        print("")
        guess_count += 1

    print(f"Sorry, you lost. Better luck next time. The correct answer was {answer}.")

if __name__ == "__main__":
    main()    

