# Final Project CS50P

#
# Noel Bohlin
#





# * Title: Popculture Hangman
# * Name: Noel Bohlin
# * GitHub username: noelbohlin
# * edX username: bohlinnoel
# * city and country: Alingsås, Sweden
# * date: 2024-01-06







import requests
from bs4 import BeautifulSoup
from imdb import Cinemagoer
from datetime import date
import random
import os
import sys


def main():
    """main"""

    # print welcome message
    intro()

    # get a word from either IMDB or Billbord hot100
    word = get_word()

    # makes the word from class imdb to string in case of movie
    # not needed in case of music
    word = str(word)

    # start game
    game(word)


def draw_man(n):
    """picture inpired by askpython.com"""

    print()
    print("\t +-------+")
    print("\t |       | ")
    print("\t {}       | ".format(n[0]))
    print("\t{}{}{}      | ".format(n[1], n[2], n[3]))
    print("\t {}       | ".format(n[4]))
    print("\t{} {}      | ".format(n[5], n[6]))
    print("\t         | ")
    print("  _______________|____")
    print("  ````````````````````")
    print()


def game(word):
    """the game loop whith input of the word"""

    clear()

    # inizializes variabels
    word_display = []
    correct_letters = []
    incorrect = []
    chances = 0

    # prints the bodyparts that will be printed later
    hangman_values = ["O", "/", "|", "\\", "|", "/", "\\"]
    show_hangman_values = [" ", " ", " ", " ", " ", " ", " "]

    # replaces word with underscores to display
    for char in word:
        if char.isalpha():
            word_display.append("_")
            correct_letters.append(char.upper())
        # if not letters then show them, like whitespace and commas
        else:
            word_display.append(char)

    # The game itself
    while True:
        # print the "galjbacke"
        draw_man(show_hangman_values)
        print()
        print("\t", end="")

        # print the underscores and then the correct letters
        for i in word_display:
            print(i, end="")
        print()
        print(f"Incorrect characters:  {incorrect}")
        print()

        input_letter = input("Enter a letter = ")

        if input_letter.upper() in incorrect:
            clear()
            print("Already tried")
            continue
        if len(input_letter) != 1:
            clear()
            print("Invalid input")
            continue
        if not input_letter.isalpha():
            clear()
            print("Not A Letter")
            continue

        if input_letter.upper() not in correct_letters:
            incorrect.append(input_letter.upper())
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
            if chances == len(hangman_values):
                print()
                clear()
                draw_man(hangman_values)
                print("The word is :", word.upper())
                print()
                print("GAME OVER!!!")
                print()
                break
        else:
            for i in range(len(word)):
                if word[i].upper() == input_letter.upper():
                    word_display[i] = input_letter.upper()

            if "_" not in word_display:
                clear()
                print("\tCongratulations! ")
                print("The word is :", word.upper())
                break
        clear()


def get_word():
    """gets word from provided list"""

    word_list = choose_category()
    chosen_difficulty = difficulty()
    if chosen_difficulty == "top25":
        return word_list[random.randint(0, 24)]
    if chosen_difficulty == "full":
        return word_list[random.randint(0, (len(word_list) - 1))]


def difficulty():
    """return difficulty"""

    while True:
        choice = input(
            'Choose difficulty, "Top25" or "Full": ').strip().lower()
        if choice == "top25" or choice == "full":
            clear()
            return choice
        else:
            print("Please try again")


def choose_category():
    """choose category between movies and songs, returns list with words"""

    while True:
        category = input(
            'Choose category, "Music" or "Movies": ').lower().strip()
        if category == "music":
            while True:
                year = input(
                    "Enter which year (YYYY) the songs should be from: "
                ).strip()
                if 1957 < int(year) < int(today()):
                    return get_billboard_hot_100(year)
                else:
                    print(
                        "year (YYYY) has to be between 1958 and the year before this year"
                    )
        if category == "movies":
            return get_imdb_top250()
        else:
            continue


def get_billboard_hot_100(year):
    """modified version of code found on github from "ihl7". return list of billboard top100"""

    date = f"{year}-08-31"
    url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    song_tags = soup.find_all(
        "h3",
        class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
    )
    songs = []
    for tag in song_tags:
        songs.append(tag.get_text().strip())
    return songs


def get_imdb_top250():
    """returns list of top250 from imdb"""

    return Cinemagoer().get_top250_movies()


def today():
    """returns this year"""

    return date.today().year


def clear():
    """clears the terminal window"""

    os.system("clear")


def intro():
    """prints a welcome message"""

    clear()
    print("     Welcome to this game of Hangman     ")
    print("   you can choose between 2 categories   ")
    print("             Movies or Music             ")
    print("                                         ")
    print("       and betwwen 2 difficulties        ")
    print("       the Top 25 of the category        ")
    print("            or the whole list            ")
    print("                                         ")
    print("                 Enyoy!                  ")
    print("\n \n \n")


if __name__ == "__main__":
    main()
