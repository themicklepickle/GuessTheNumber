# Assignment - Guess a Number Game
# Interface module
# Michael Xu
# May 1, 2020

# import all functions from modules
from graphics import *
from calculations import *

again = 1

while again:

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

	print(winner)  # displays the winner

	print(guesses)  # prints the number of guesses used

	again = play_again()
