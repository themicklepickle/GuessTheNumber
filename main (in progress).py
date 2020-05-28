# Assignment - Guess a Number Game
# Interface module
# Michael Xu
# May 1, 2020

# import all functions from modules
from School.Assignments.guess_the_number.graphics import *
from School.Assignments.guess_the_number.calculations import *
from datetime import date, datetime

again = True

while again:
	txt_file = open("data.txt", "a")
	csv_file = open("data.csv", "a")

	main_screen()  # display main screen
	draw_levels()  # draw levels and their ranges in the left column

	level = int(level_choice())  # input choice for level
	select_level(level)  # surround chosen level in green

	player_scope = scope(level)  # find scope of level
	computer_scope = player_scope  # set initial scopes of player and computer to the same range

	player_description(player_scope)  # write player scope and target
	computer_description(computer_scope)  # write computer scope and target

	player_target = random_num(player_scope)  # generate random number for player target
	computer_target = choose_computer_target(computer_scope)  # input computer target from user

	computer_description(computer_scope, computer_target)  # rewrite computer description to include target

	winner, guesses = guessing_algorithm(player_target, player_scope, computer_target, computer_scope)  # run guessing algorithm

	display_winner(winner, guesses)  # display winner and the number of guesses

	txt_file.write(f"date: {date.today().strftime('%m/%d/%y')}, time: {datetime.now().strftime('%H:%M:%S')}, level: {level}, winner: {winner}, guesses: {str(guesses)}\n")
	csv_file.write(f"{date.today().strftime('%m/%d/%y')},{datetime.now().strftime('%H:%M:%S')},{level},{winner},{guesses}\n")

	txt_file.close()
	csv_file.close()

	again = play_again()
