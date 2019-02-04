from random import randint, choice

BATTLESHIP = [4, ["T", 1]]
FIGHTER = [3, ["F", 2]]
SUBMARINE = [2, ["S", 3]]
BOMBER = [1, ["B", 4]]
c_bomb = []
val = []
counter = []

board = []

for x in range(0, 10):
    board.append([str(x)]+["O"] * 10)

def print_board(board):
    print("  1 2 3 4 5 6 7 8 9 10")
    for row in board:
        print((" ").join(row))

def random_row(board):
    return randint(1, len(board) - 1)

def random_col(board):
    return randint(1, len(board[0]) - 1)


def set_bomber(ship):
    while len(c_bomb) != ship[1][1] * ship[0]:
        rand_orient = choice(["R", "C"])
        ship_row = random_row(board)
        ship_col = random_col(board)
        for i in range(ship[0]):
            if (ship_row + ship[0]-1 <= 9) and (ship_col + ship[0]-1 <= 10 ):
                if rand_orient == "R":
                    if board[ship_row][ship_col+i] == "O":
                        board[ship_row][ship_col+i] = ship[1][0]
                        counter.append("W")
                        c_bomb.append(ship[1][0])
                        val.append([ship_row, ship_col])
                else:
                    if board[ship_row][ship_col+i] == "O":
                        board[ship_row+i][ship_col] = ship[1][0]
                        counter.append("W")
                        c_bomb.append(ship[1][0])
                        val.append([ship_row, ship_col])
        print(ship_row, ship_col)
    print(c_bomb)
    c_bomb.clear()
    print(c_bomb)
print_board(board)


if __name__ == '__main__':
    print_board(board)
    set_bomber(BOMBER)
    count = 0
    run = True
    while run:
        row = int(input("ROW: "))
        col = int(input("COL: "))
        print(val , [row, col] )
        if len(counter) == count:
            run = False
            print("YOU DESTROYED MY BATTLESHIP!")
        if [row, col] in  val:
            print("yes")
            board[row][col] = "X"
            count += 1
        else:
            if board[row][col] == ".":
                print("used before")
            else:
                board[row][col] = "."
                print("miss")
        print_board(board)
        

            
        
