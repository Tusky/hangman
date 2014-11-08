import os
import random

word_list = open('wordlist.txt')
words = word_list.readlines()
letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
hangman = ["      \n      \n      \n      \n", "    | \n    | \n    | \n   _|_\n", "    | \n    | \n    | \n   _|_\n",
           "----| \n    | \n    | \n   _|_\n", "----| \n o  | \n    | \n   _|_\n", "----| \n o  | \n |  | \n   _|_\n",
           "----| \n o  | \n\|  | \n   _|_\n", "----| \n o  | \n\|/ | \n   _|_\n", "----| \n o  | \n\|/ | \n/  _|_\n",
           "----| \n o  | \n\|/ | \n/\ _|_\n"]


def menu():
    os.system('cls') if "windows" in os.name.lower() else os.system('clear')
    choice = 0
    while not 5 >= choice > 1:
        choice = int(raw_input("1: Start Game\n2: Add Word\n3: List Words\n4: Remove Words\n"
                               "5: List words by given length\n6: Exit\n\nChoose: "))
    if choice == 1:
        start_game()
    elif choice == 2:
        add_word()
    elif choice == 3:
        list_words()
    elif choice == 4:
        remove_word()
    elif choice == 5:
        list_words_by_length()
    elif choice == 6:
        save_words()
        exit()


def save_words():
    word_file = open('wordlist.txt', 'w')
    words.sort()
    for word in words:
        word_file.write("%s" % word.lower())
    word_file.close()


def remove_word():
    word = raw_input("Type your word here that you'd like to remove: ")
    if word + '\n' in words:
        words.remove(word + '\n')
    else:
        print 'The word you were looking for was not found.'
    raw_input("Your word has been added to the list. Press enter to continue...")
    menu()


def list_words(words_to_list=words):
    words_to_list = [word.strip() for word in words_to_list]
    print ', '.join(words_to_list)
    raw_input("Press enter to continue")
    menu()


def list_words_by_length():
    char_length = int(raw_input("How long the word should be?"))
    words_to_list = []
    for word in words:
        if len(word.strip()) == char_length:
            words_to_list.append(word.strip())
    print ', '.join(words_to_list)
    raw_input("Press enter to continue")
    menu()


def add_word():
    word = raw_input("Type your word here: ")
    if word not in words:
        words.append(word + '\n')
    raw_input("Your word has been added to the list. Press enter to continue...")
    menu()


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
    start_game() if raw_input("Do you want to play again? y/n: ") in ['y', 'Y'] else menu()


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
        print hangman[lives]
        print "Possible letters to guess: %s\n\n%s\n" % (game_letters, game_word)
        guess_letter = raw_input('Guess a letter: ')
        guess_letter = guess_letter[0] if len(guess_letter) > 0 else False
        if is_valid_letter(guess_letter):
            if guess_letter.upper() in guessed_letters:
                print 'Already guessed that letter!'
                continue
            guessed_letters.append(guess_letter.upper())
            game_letters = game_letters.replace(guess_letter.upper() + ' ', '')
        if game_word == get_game_word(word, guessed_letters):
            lives += 1
    print "You have lost the game, the word was %s!" % word
    play_again()


menu()