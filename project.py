import curses

def main(stdscr):
    # Turn off echoing of keys, and enter cbreak mode,
    # where no buffering is performed on keyboard input
    curses.cbreak()

    # Turn off automatic echoing of keys to the screen
    curses.noecho()

    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Initialize the current player
    current_player = 'X'

    # Initialize the game loop
    while True:
        # Clear the screen
        stdscr.clear()

        # Draw the board
        for i in range(3):
            for j in range(3):
                stdscr.addstr(i, j * 3, board[i][j])

        # Draw the current player
        stdscr.addstr(10, 10, f'Current player: {current_player}')

        # Refresh the screen to display changes
        stdscr.refresh()

        # Wait for user input
        event = stdscr.getkey()

        # Check if the user wants to quit
        if event == 'q':
            break

        # Parse the user input
        try:
            row, col = map(int, event[1:-1].split(','))
            row -= 1
            col -= 1
        except:
            continue

        # Place the current player's mark on the board
        board[row][col] = current_player

        # Check if a player has won
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                stdscr.addstr(12, 10, f'Player {current_player} wins!')
                stdscr.refresh()
                break

        # Switch to the other player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        # Wait for user input before continuing
        stdscr.getkey()

    # Clean up before exiting
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# Run the game
curses.wrapper(main)
