# Film Quiz

import csv  # CSV file reader/writer
import sys  # allows use of sys.exit command
import random  # random film selection from readlines
import time  # for pauses

# MAIN


def main():
    menu()


# MENU
def menu():
    score = 0
    print()
    menuinput = input("""
        ***********MAIN MENU***********

                1: Play Film Quiz
                2: View Leaderboard
                3: Exit

                Please enter your choice: """)

    # if the choice is 1, 2, 3, go to the subroutine
    if menuinput == "1":
        quiz(score)
    elif menuinput == "2":
        leaderboard()
    elif menuinput == "3":
        print("""

        Thank you for playing Film Quiz - Now shutting down...
        """)
        time.sleep(3)
        raise SystemExit
    else:
        # if an invalid option was selected, repeat menu
        print("""

        You must only select from 1, 2 or 3""")
        # return to menu
        menu()

# QUIZ


def quiz(score):
    tries = 0

    file = open("films.txt", "r")
    filmList = file.readlines()  # read lines from file
    file.close()

    # selects random line, removes spaces, then splits line into array at " - "
    randomSelection = random.choice(filmList)
    randomSelection = randomSelection.strip().split(" - ")

    director = randomSelection[0]

    film = randomSelection[1]

    print("")
    print("  GUESS THE FILM ++++++++++++++++++++++")

    codedFilm = ""

    # loops for every character in film string, adds "_" or space to codedString (covered version of film for quiz)
    for x in film:
        if x == " ":
            codedFilm += "  "
        else:
            codedFilm += "_ "

    # replaces first "_" with actual character from film string - a hint
    codedFilm = codedFilm.replace("_ ", str(film[0]) + " ", 1)

    # while loops exits after 3 tries (or begins quiz() again at win)
    while tries < 3:

        print("")
        print("  Current score: " + str(score))
        print("")
        print("  DIRECTOR: " + director)
        print("  FILM: " + codedFilm)
        print("")
        guess = input("  Enter your guess: ")

        if guess.lower() == film.lower():
            print("")
            print("  ✓ CORRECT - The film was " + film + " by " + director)
            print("")
            print("  Ready for the next one?")
            print("")
            print("  -------------------------")
            score += 50
            quiz(score)
        else:
            print("")
            print("  ╳ INCORRECT - Too bad, try again!")
            print("")
            print("  -------------------------")
            score -= 10
            tries += 1

    print("")
    print("Your final score was: " + str(score))
    print("")

    # if score is greater than 0, allow user to add to the leaderboard
    if score > 0:
        print("Would you like to add your score to the leaderboard?")
        scoreInput = input("\n[Y]es/[N]o: ")

        if scoreInput == ("y") or scoreInput == ("Y"):

            userInput = input("Choose a name for the leaderboard: ")

            # writing user and score to the leaderboard
            file = open("leaderboard.txt", "a")
            file.write("\n" + userInput + " " + str(score))
            file.close()

            # takes user back to the menu
            print("")
            print("Your score has been added to the leaderboard.")
            print("")
            print("Now returning to the menu...")
            time.sleep(3)

    # return to menu
    menu()


# LEADERBOARD
def leaderboard():
    # open leaderboard
    file = open("leaderboard.txt", "r")
    # create a leaderboard list to load all lines into
    displayleaderboard = file.read()
    # print the list
    print("")
    print("---------------------------")
    print("      LEADERBOARD")
    print("---------------------------")
    print("")
    print(displayleaderboard)
    file.close()
    menu()


# Begin program with main
main()
