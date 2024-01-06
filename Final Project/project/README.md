# Hangman

Name: Noel Bohlin | Country: Sweden | City: Alingsås | github: noelbohlin | edx: bohlinnoel

## Video Demo: <https://www.youtube.com/watch?v=VaZfejdJlGw>

## Description

This project is a simple game of hangman, but using different libraries to create a quite nice to play game for being in a terminal.

I wanted you to be able to choose both theme and difficulty before a game, and this is possible. If movies are chosen as categories you can now choose between either the top25 movies or the top 250 movies from IMDB. If music is chosen you can first choose which year you want the list to be from. between 1958 and today, then the difficulty between top25 and top100. When the game is started you are allowed 6 wrong letters before the last try.

The game aesthetics are heavily inspired by the website askpython. the way the man is drawn and the display method is a modified version of theirs. The billboard web scraper is coded by me. But the search terms to find the right html hotwords are copied from "ihl7" from github. apart from these inspirations the code is original.

I decided to put all the functions in the project.py for the simplicity even if some smaller functions like today(), whose only function is to get today's date, made it quite messy. I decided to use multiple functions instead of a long main to compartmentalize my code and make it easier to debug even if there are now a lot of functions buried in other functions and so on.

### Function explanations

#### The function clear

```python
def clear():
   """clears the terminal window"""


   os.system("clear")
```

is used quite frequently to create a more visualy pleasing experience for the player. To include this was quite an easy choice and it creates the illusion of a changing display instead of a terminal.

#### IMDb

```python
pip install git+https://github.com/cinemagoer/cinemagoer
from imdb import Cinemagoer
```

I used the library Cinemagoer to access the IMDb website. I tried to build my own scraper but failed, the website wasn't structured the same way as the billboard hot 100 and I dont have the know-how to know how to build the right search terms. But then I found the library IMDbPy and then this continuation. It seems to be quite buggy and doesn't work 100% of the time. But it has at least worked for 2 days in a row now.

The decision to implement a difficulty function was to make the words more recongiseble for kids, as the 249th most popular movie isn't that famous.

#### BillBoard Hot 100

```python
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
```

When choosing the category "music" in this function you get the choice of year. This was to further add to the customizability of the word list. This chooses a date in August of the chosen year as I thought it was most representable. I could of course make it possible for the player to choose their own date. but i thought that would make too many choices for just a simple game of hangman.
