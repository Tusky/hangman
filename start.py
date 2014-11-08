import os
import random

wordlist = open('wordlist.txt')
words = wordlist.readlines()
letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
hangmans = ["      \n      \n      \n      \n", "    | \n    | \n    | \n   _|_\n", "    | \n    | \n    | \n   _|_\n",
            "----| \n    | \n    | \n   _|_\n", "----| \n o  | \n    | \n   _|_\n", "----| \n o  | \n |  | \n   _|_\n",
            "----| \n o  | \n\|  | \n   _|_\n", "----| \n o  | \n\|/ | \n   _|_\n", "----| \n o  | \n\|/ | \n/  _|_\n",
            "----| \n o  | \n\|/ | \n/\ _|_\n"]


def is_valid_letter(letter):
    if letter.upper() in letters:
        return True
    return False


def get_game_word(word, letters_guessed):
    word_to_print = ""
    for letter in word:
        if letter.upper() in letters_guessed:
            word_to_print += letter + ' '
            continue
        word_to_print += '_ '
    return word_to_print


def check_win(game_word, word):
    if '_' not in game_word:
        print "You have won, the word was %s!" % word
        play_again()


def play_again():
    start_game() if raw_input("Do you want to play again? y/n:") in ['y', 'Y'] else exit()


def get_random_word(length=0):
    random_word = random.choice(words)
    if length > 0:
        while len(random_word) != length + 1:
            random_word = random.choice(words)
    return random_word.strip()


def start_game(lives=0, game_letters=letters):
    guessed_letters = []
    try:
        word = get_random_word(int(raw_input("How long the word should be?")))
    except ValueError:
        word = get_random_word()
    while lives < 10:
        os.system('cls') if "windows" in os.name.lower() else os.system('clear')
        game_word = get_game_word(word, guessed_letters)
        check_win(game_word, word)
        print hangmans[lives]
        print "Possible letters to guess: %s\n\n%s\n" % (game_letters, game_word)
        guess_letter = raw_input('Guess a letter: ')
        guess_letter = guess_letter[0] if len(guess_letter) > 0 else False
        if is_valid_letter(guess_letter):
            if guess_letter.upper() in guessed_letters:
                print 'Already guessed that letter'
                continue
            guessed_letters.append(guess_letter.upper())
            game_letters = game_letters.replace(guess_letter.upper() + ' ', '')
        if game_word == get_game_word(word, guessed_letters):
            lives += 1
    print "You have lost the game, the word was %s" % word
    play_again()


start_game()