Hangman Game

Welcome to the Hangman Game! This simple Python script allows you to play the classic Hangman game with a random word chosen from a predefined list.
How to Play

    Run the script in a Python environment.
    You will be prompted to enter your guess letter.
    Guess letters one at a time and try to uncover the hidden word.
    Be careful! Incorrect guesses will cost you lives, and you have a total of 6 lives.
    The game ends when you either successfully guess the word or run out of lives.

Hangman Stages

The game provides visual representations of your hangman state as you progress. The stages are displayed in ASCII art, depicting the hangman's status.

Here are the different stages:

Stage 1

    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========

Stage 2

    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========

Stage 3

    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========

Stage 4

    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========

Stage 5

    +---+
    |   |
    O   |
    |   |
        |
        |
    =========

Stage 6

    +---+
    |   |
    O   |
        |
        |
        |
    =========


Stage 7

    +---+
    |   |
        |
        |
        |
        |
    =========

Word List

The game randomly selects a word from the following list:

    aardvark
    baboon
    camel

Feel free to modify the word_list in the code to include more words or change the existing ones.

Have fun playing Hangman!
