import random
import turtle


def scope(level):
	if level == 4:
		return int(turtle.numinput("Scope", "Scope Lower Bound (int):")), int(turtle.numinput("Scope", "Scope Upper Bound (int):"))
	else:
		levels = {1: (1, 100), 2: (1, 1000), 3: (1, 10000)}
		return levels[level]


def random_num(scope):
	return random.randint(scope[0], scope[1])


def choose_computer_target(scope):
	return int(turtle.numinput("Computer Target", f"Computer Target ({scope[0]} - {scope[1]}):", minval=scope[0], maxval=scope[1]))