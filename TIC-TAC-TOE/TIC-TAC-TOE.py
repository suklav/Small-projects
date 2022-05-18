
def main():
    print()
    print("Welcome to TIC TAC TOE!")
    print()
    print("(Row and column number starts with a zero)")
    print()


    
    matrix = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

    # api variable is nothing but the index of current or active player.. LOL:)
    api = 0
    p1= input("Hello! \nEnter player1 name: ")
    p2= input("Hello! \nEnter player2 name: ")
    
    players = [p1,p2]
    
    
    symbols = ["X", "O"]
    player = players[api]

    # UNTIL SOMEONE WINS
    while not tictactoe(matrix):
        # SHOW THE matrix
        player = players[api]
        symbol = symbols[api]

        announce_turn(player)
        show_matrix(matrix)
        if not choose_location(matrix, symbol):
            print("That isn't an option, try again.")
            continue

        # TOGGLE ACTIVE PLAYER
        api = (api + 1) % len(players)

    print()
    print(f"GAME OVER! {player} has won with the matrix: ")
    show_matrix(matrix)
    print()


def choose_location(matrix, symbol):
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))

    row -= 1
    column -= 1
    if row < 0 or row >= len(matrix):
        return False
    if column < 0 or column >= len(matrix[0]):
        return False

    cell = matrix[row][column]
    if cell is not None:
        return False

    matrix[row][column] = symbol
    return True


def show_matrix(matrix):
    for row in matrix:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the matrix:")
    print()


def tictactoe(matrix):
    sequences = get_winning_sequences(matrix)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False


def get_winning_sequences(matrix):
    sequences = []

    # Win by rows
    rows = matrix
    sequences.extend(rows)

    # Win by columns
    for col_idx in range(0, 3):
        col = [
            matrix[0][col_idx],
            matrix[1][col_idx],
            matrix[2][col_idx],
        ]
        sequences.append(col)

    # Win by diagonals
    diagonals = [
        [matrix[0][0], matrix[1][1], matrix[2][2]],
        [matrix[0][2], matrix[1][1], matrix[2][0]],
    ]
    sequences.extend(diagonals)

    return sequences


if __name__ == '__main__':
    main()
