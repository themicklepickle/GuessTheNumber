# Assignment - Guess a Number Game
# Graphics module
# Michael Xu
# May 1, 2020

import random

# turtle setup
import turtle
turtle.setup(width=1.0, height=1.0, startx=0, starty=0)
turtle.title("Guess the Number!")
turtle.shape("blank")
turtle.clear()
turtle.pencolor("black")
turtle.pensize(4)
turtle.speed(0)

p_description = turtle.Turtle()
p_description.shape("blank")
p_description.speed(0)

c_description = turtle.Turtle()
c_description.shape("blank")
c_description.speed(0)

player_log = turtle.Turtle()
player_log.speed(0)
player_log.shape("blank")

computer_log = turtle.Turtle()
computer_log.speed(0)
computer_log.shape("blank")


def text(x, y, text, font_size, colour="black", weight="normal", font="Arial", turtle_name=turtle):
	turtle_name.up()
	turtle_name.pencolor(colour)
	turtle_name.setpos(x, y)
	turtle_name.write(text, font=(font, font_size, weight))


def rectangle(lower_left, upper_right, colour):
	turtle.pencolor(colour)
	turtle.up()
	turtle.setpos(lower_left[0], upper_right[1])
	turtle.pendown()
	turtle.setpos(lower_left[0], lower_left[1])
	turtle.setpos(upper_right[0], lower_left[1])
	turtle.setpos(upper_right[0], upper_right[1])
	turtle.setpos(lower_left[0], upper_right[1])


def line(start, end, colour="black"):
	turtle.pencolor(colour)
	turtle.up()
	turtle.setpos(start[0], start[1])
	turtle.down()
	turtle.setpos(end[0], end[1])


def main_screen():
	turtle.clear()
	p_description.clear()
	c_description.clear()
	player_log.clear()
	computer_log.clear()

	text(-240, 280, "Guess the Number!", 50, weight="bold")
	text(-120, 240, "A Michael & Rob Co. Game", 20)

	line((-220, 200), (-220, -320))
	line((220, 200), (220, -320))

	text(-490, 150, "Level", 40)
	text(-55, 150, "Player", 40)
	text(340, 150, "Computer", 40)


def draw_level(level_number, colour="black"):
	levels = {1: {"scope": "1-100", "text_x_pos": -526},
			  2: {"scope": "1-1000", "text_x_pos": -532},
			  3: {"scope": "1-10000", "text_x_pos": -540},
			  4: {"scope": "custom", "text_x_pos": -535}}

	spacing = 110
	rectangle((-550, -290 + spacing * (4 - level_number)), (-350, -240 + spacing * (4 - level_number)), colour)
	text(levels[level_number]["text_x_pos"], 50 - spacing * (level_number - 1),
		 f'Level {level_number}: {levels[level_number]["scope"]}', 25, "black")


def draw_levels():
	draw_level(1)
	draw_level(2)
	draw_level(3)
	draw_level(4)


def select_level(level):
	draw_level(level, "green")


def level_choice():
	return turtle.numinput("Level", "Choose a level (1-4):", minval=1, maxval=4)


def player_description(scope, target="???", win=False):
	p_description.clear()
	if win:
		text(-200, 100, f"Target: {target}", 25, "green", turtle_name=p_description)
	else:
		text(-200, 100, f"Target: {target}", 25, turtle_name=p_description)
	text(-200, 60, f"Scope: {scope[0]} - {scope[1]}", 25, turtle_name=p_description)


def computer_description(scope, target="", win=False):
	c_description.clear()
	if win:
		text(240, 100, f"Target: {target}", 25, "green", turtle_name=c_description)
	else:
		text(240, 100, f"Target: {target}", 25, turtle_name=c_description)
	text(240, 60, f"Scope: {scope[0]} - {scope[1]}", 25, turtle_name=c_description)


def write_player_log(guesses):
	player_log.clear()
	for i in range(len(guesses)):
		text(-200, -10 - 40 * i, f"Guess: {guesses[i]}", 25, turtle_name=player_log)


def write_computer_log(guesses):
	computer_log.clear()
	for i in range(len(guesses)):
		text(240, -10 - 40 * i, f"Guess: {guesses[i]}", 25, turtle_name=computer_log)


def display_winner(winner, guesses):
	if winner == "player":
		text(-60, 190, "WINNER!", 30, "green")
	if winner == "computer":
		text(365, 190, "WINNER!", 30, "green")
	if winner == "tie":
		text(195, 210, "TIE!", 30, "green")
	text(350, 280, f"Guesses: {guesses}", 30, "green")


def organize_list(guess_list, guess):
	if len(guess_list) < 8:
		guess_list.append(guess)
	else:
		guess_list.pop(0)
		guess_list.append(guess)
	return guess_list


def new_scope(old_scope, guess, target):
	if guess < target:
		updated_scope = (guess + 1, old_scope[1])
	elif guess > target:
		updated_scope = (old_scope[0], guess - 1)
	else:
		updated_scope = old_scope
	return updated_scope


def guessing_algorithm(player_target, player_scope, computer_target, computer_scope):
	player_guess = player_target - 1
	computer_guess = computer_target - 1
	player_guess_list = []
	computer_guess_list = []
	guesses = 0

	while player_guess != player_target and computer_guess != computer_target:
		guesses += 1
		player_description(player_scope)
		computer_description(computer_scope, computer_target)

		player_guess = int(turtle.numinput("Guess", f"Guess ({player_scope[0]} - {player_scope[1]}):", minval=player_scope[0], maxval=player_scope[1]))
		computer_guess = int(random.randint(computer_scope[0], computer_scope[1]))

		player_guess_list = organize_list(player_guess_list, player_guess)
		computer_guess_list = organize_list(computer_guess_list, computer_guess)

		write_player_log(player_guess_list)
		write_computer_log(computer_guess_list)

		player_scope = new_scope(player_scope, player_guess, player_target)
		computer_scope = new_scope(computer_scope, computer_guess, computer_target)

	if player_guess == player_target and computer_guess == computer_target:
		player_description(player_scope, player_target, True)
		computer_description(computer_scope, computer_target, True)
		return "tie", guesses
	elif player_guess == player_target:
		player_description(player_scope, player_target, True)
		return "player", guesses
	elif computer_guess == computer_target:
		computer_description(computer_scope, computer_target, True)
		player_description(player_scope, player_target)
		return "computer", guesses


def play_again():
	return turtle.numinput("Play Again?", "Yes (1) or No (0):", minval=0, maxval=1)



