import sys
import time
import os
import random

### Terminal TIC TAC TOE ###
# v 1.0
# single player
# multiplayer soon
# add game stats: avg time to move, total length, number of invalid moves 
# add help option

# 0 = blank, 1 = 'O', 9 = 'X' 
def rand_start():
	r = random.random()
	if r < 0.5:
	 	return 1
	return 9

def name(num_player, players):
	# use player names
	if num_player == 9:
		return players[0]
	elif num_player == 1:
		return players[1]
	else:
		return "NOBODY"

def change_player():
	if player == 1:
		return 9
	return 1

def type_writer(string, t=0.1):
	for letter in string:	
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(random.uniform(0, t))
	print("")

def clean_type_writer(string, t=0.03):
	for letter in string:
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(t)
	print("")

def game_check(board, size):

	# check columns and rows in one pass
	s = [0 for _ in range(size)]
	zeros = 0
	for i in range(size):
		for j in range(size):

			row = board[j]
			s[i] += row[i]
			if row[i] == 0:
				zeros += 1
			# check row at the beginning
			if i == 0:
				val = sum(row)
				if val == 27:
					return (True, 9)
				elif val == 3:
					return (True, 1)
	# check diagonals
	td = board[0][0] + board[1][1] + board[2][2]
	du = board[0][2] + board[1][1] + board[2][0]
	s.append(td)
	s.append(du)

	for elem in s:
		if elem == 27:
			# X wins
			return (True, 9)
		elif elem == 3:
			# O wins
			return (True, 1)
	# check for catsgame
	if zeros == 0:
		return (True, 'Nobody')

	return [False]

def conversion(char):
	if char == 0:
		return ' '
	elif char == 1:
		return 'O'
	elif char == 'Nobody':
		return char
	else:
		return "X"

def print_board(board, size):
	rows = []
	# O | O | X
	line = "|-----------|"
	for row in board:
		string = "|"
		for char in row:
			string += " " + conversion(char) + " |"
		rows.append(string)

	print(line)
	for r in rows:
		print(r)
		print(line)

def coord_translate(coord):
	try:
		if len(coord) != 2:
			return "INVALID MOVE"
		elif (int(coord[0]) >= size or int(coord[0]) < 0) or (int(coord[1]) >= size or int(coord[1]) < 0):
			return "INVALID MOVE"
		else:
			return [size - 1 - int(coord[1]), int(coord[0])]
	except:
		return "INVALID MOVE"

def start_game():
	os.system("clear")
	h = open("header.txt", "r")
	r = open("rules.txt", "r")

	text = h.read()
	rules = r.read()

	clean_type_writer(text, 0.002)
	time.sleep(0.2)

	type_writer(rules)
	type_writer("All Good?")
	response = input()

	count = 0
	while response.lower() not in ["yup", "yes", "yeah", "ye", "y", "yea", "yep", "yee", "yeee", "yus", "yas"]:
		# add regex
		if count > 7:
			type_writer("\nAlright this is ridiculous...")
			time.sleep(2)
			break
		else:
			time.sleep(1)
			type_writer("\nHow About Now?")
		count += 1 
		response = input()

	print("\nPlayer X name:")
	x = input()
	print("\nPlayer O name:")
	o = input()

	os.system("clear")
	type_writer("LETS DO THIS!")
	return (x, o)

def end_game(winner):
	e = open("end.txt", "r")
	txt = e.read()

	time.sleep(0.1)
	os.system("clear")
	print_board(board, size)
	type_writer("THE WINNER IS " + winner + "!!!!")
	clean_type_writer(txt, 0.004)

def best_move(board, size, player):
	# find the best location of a move given current board and player
	return "11"


if __name__ == "__main__":
	moves = []
	turns = 0
	board =  [[0,0,0],
              [0,0,0],
              [0,0,0]]
	size = len(board)

	player = rand_start()
	players = start_game()

	print_board(board, size)
	while (True):
		result = game_check(board, size)
		if (result[0]):
			end_game(name(result[1], players))
			break

		# Wait for valid move
		print("\n" * 13)
		type_writer(name(player, players) + "'s (" + conversion(player) + ") Move:")
		raw_move = input()
		move = coord_translate(raw_move)
		while raw_move in moves or type(move) == str:
			type_writer("INVALID MOVE " + str(raw_move))
			print_board(board, size)
			print("\n" * 19)
			type_writer(name(player, players) + "'s (" + conversion(player) + ") Move:")
			
			raw_move = input()
			move = coord_translate(raw_move)

		moves.append(raw_move)
		
		board[move[0]][move[1]] = player
		turns += 1
		player = change_player()
		os.system("clear")
		print_board(board, size)
		




