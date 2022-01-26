"""

# Simple implementation on Tic Tac Toe in python
# This will form the back end 
# Arguments: none
# Author: Arun Vijayshankar

"""

def initGrid():
	rows, cols = (3, 3)
	grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	return grid

def getPlayers():
	player1 = input("Choose X or O: ")
	if player1 == 'X':
		player2 = 'O'
	elif player1 == 'O':
		player2 = 'X'
	else:
		player1 = input("Invalid choice. Choose between X or O: ")
	return [player1, player2]

def moves(grid, player):
	#empBoxes = getEmptyBoxes(grid)
	gMap = dict([('a1', [0, 0]), ('a2', [0, 1]), ('a3', [0, 2]), ('b1', [1, 0]), ('b2', [1, 1]), ('b3', [1, 2]), ('c1', [2, 0]), ('c2', [2, 1]), ('c3', [2, 2])])
	key_list = list(gMap.keys())
	val_list = list(gMap.values())
	move = input("Choose one from unmarked boxes: ");
	if move not in key_list:
		move = input("Invalid choice. Please choose from list of unmarked boxes")
	else:
		grid[gMap[move][0]][gMap[move][1]] = player

def checkGrid(grid):
	if checkDiags(grid):
		return 1
	elif checkRows(grid):
		return 1
	elif checkCols(grid):
		return 1
	else:
		return 0
def checkRows(grid):
	for i in range(3):
		if (grid[i].count('X') == 3) or (grid[i].count('O') == 3):
			return 1
	return 0

def checkCols(grid):
	for i in range(3):
		col = Column(grid, i)
		if (col.count('X') == 3) or (col.count('O') == 3):
			return 1
	return 0

def Column(grid, i):
	return [row[i] for row in grid]

def checkDiags(grid):
	diags = [[grid[0][0], grid[1][1], grid[2][2]], [grid[0][2], grid[1][1], grid[2][0]]]
	for i in range(2):
		if (diags[i].count('X') == 3) or (diags[i].count('O') == 3):
			return 1
	return 0

def getEmptyBoxes(grid):
	list = []
	for i in range(3):
		for j in range(3):
			if grid[i][j] == ' ':
				list.append([i, j])
	return list

def Game(grid):
	numMoves = 0
	players = getPlayers()
	printNice(grid)
	moves(grid, players[numMoves % 2])
	numMoves += 1
	printNice(grid)
	while (numMoves < 9):
		if checkGrid(grid):
			print("player " + str(players[(numMoves+1) % 2]) + " wins!")
			break
		moves(grid, players[numMoves % 2])
		numMoves += 1
		printNice(grid)
	if numMoves == 9:
		print("game is a draw")

def printNice(grid):
	print("    1   2   3")
	print("a | " + str(grid[0][0]) + " | " + str(grid[0][1]) + " | " + str(grid[0][2]) + " | ")
	print("  --------------")
        print("b | " + str(grid[1][0]) + " | " + str(grid[1][1]) + " | " + str(grid[1][2]) + " | ")
        print("  --------------")
        print("c | " + str(grid[2][0]) + " | " + str(grid[2][1]) + " | " + str(grid[2][2]) + " | ")


if __name__ == "__main__":
	grid = initGrid()
	Game(grid)

