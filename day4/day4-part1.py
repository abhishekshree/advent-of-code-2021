infile = "input2.txt"

moves = []
boards = []
with open(infile, "r") as f:
    lines = f.readlines()
    moves = list(map(int, lines[0].split(",")))
    cnt = 0
    board = []
    for l in range(2, len(lines)):
        if lines[l] != '\n':
            board.append(list(map(int, lines[l].rstrip('\n').split(" "))))
        else:
            boards.append(board)
            board = []
    boards.append(board)

checkboxes = [[[False for x in range(5)] for y in range(5)] for x in range(len(boards))]

def check_win(checkbox):
    ok = False
    for x in range(5):
        if checkbox[x][0] == True and checkbox[x][1] == True and checkbox[x][2] == True and checkbox[x][3] == True and checkbox[x][4] == True:
            ok = True
    
    for y in range(5):
        if checkbox[0][y] == True and checkbox[1][y] == True and checkbox[2][y] == True and checkbox[3][y] == True and checkbox[4][y] == True:
            ok = True
    
    return ok

def mark(n):
    for z in range(len(boards)):
        for x in range(5):
            for y in range(5):
                if boards[z][x][y] == n:
                    checkboxes[z][x][y] = True
                
def check_winner():
    for c in checkboxes:
        if check_win(c):
            return checkboxes.index(c)

win_num = -1
win_board_idx = -1
win_board = []

for m in moves:
    mark(m)
    c = check_winner()
    if c != None:
        win_num = m
        win_board_idx = c
        break

win_board = boards[win_board_idx]

print("Winning number:", win_num)
print("Winning board:", win_board)

s = 0
for x in range(5):
    for y in range(5):
        if checkboxes[win_board_idx][x][y] == False:
            s += win_board[x][y]

print("Result: ", s*win_num)
