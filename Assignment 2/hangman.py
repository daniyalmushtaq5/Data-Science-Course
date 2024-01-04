import random

def hangman_state(live):
    stages = [
                '''
                +---+
                |   |
                O   |
                /|\  |
                / \  |
                    |
                =========
                ''', 

                '''
                +---+
                |   |
                O   |
                /|\  |
                /    |
                    |
                =========
                ''', 

                '''
                +---+
                |   |
                O   |
                /|\  |
                    |
                    |
                =========
                ''', 

                '''
                +---+
                |   |
                O   |
                /|   |
                    |
                    |
                =========
                ''', 

                '''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========
                ''', 

                '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========
                ''', 

                '''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========
                '''
            ]
    return stages[live]



def hangman(word_list):
    chosen_word = random.choice(word_list)
    display = ["_" for _ in chosen_word]
    live = 6

    while(True):
        guess = input("Enter your guess letter: ").lower()
        if guess in chosen_word:
            if guess not in display:
                for count,letter in enumerate(chosen_word):
                    if guess == letter:
                        display[count] = guess

                if "_" not in display:
                    guess_word = "".join(display)
                    print(f"Your live stage is\n{hangman_state(live)}\n")
                    return f"Your Guess word is {guess_word}\nCongratulations!!! Your Are Won"
                else:
                    print(display)
            else:
                print("You have already guessed this letter.")

        else:
            live -= 1
            if live == 0:
                return f"Your live stage is\n{hangman_state(live)}\n.You Lose.Your have consumed all lives"
            else:
                print(f"Your Guess Letter {guess} is not present in a Word\nYour remaining lives are {live} Please Try Again :)")



if __name__ == "__main__":
    print("Welcome to Hangman Game\n")
    word_list = ["aardvark", "baboon", "camel"]
    hangman = hangman(word_list)
    print(hangman)

    
        

