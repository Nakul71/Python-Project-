# Python-Project-
Tic-Tac-Toe Game with GUI
This project is a graphical implementation of the classic Tic-Tac-Toe game using Python's Tkinter library. It allows two players to play the game on the same system and tracks the game state to determine the winner or a tie.

# Features
Two-player Mode: Players "X" and "O" take turns.

Dynamic Turn Indication: The game updates the turn indicator dynamically.

Winner Highlighting: Highlights the winning line when a player wins.

Tie Detection: Detects and declares a tie when all cells are filled without a winner.

Restart Functionality: A restart button to reset the game board for a new game.

Winner Recording: Saves the winner of each game to a winners.txt file.

# How It Works
The game board is a 3x3 grid of buttons.

Players take turns clicking on empty cells.

The game checks for a win, tie, or continuation after each turn.

The winning combination is highlighted in green, and a tie turns the grid blue.

The "Restart" button resets the board for a new game.

Each game's winner is saved to the file winners.txt.

# Requirements

Python 3.x

Tkinter (pre-installed with Python)

# How to Run

Save the project.py file in your project directory.

Run the file using Python:

bash

Copy

Edit

python project.py

A GUI window will open where you can start playing.
Project Files

project.py: Main script containing the game logic and GUI implementation.

winners.txt: File to store the names of winners (created automatically after the first game).

# Game Rules

The first player is chosen randomly as "X" or "O".

Players alternate turns, marking one cell per turn.

# The game ends when:

A player aligns three marks horizontally, vertically, or diagonally.

All cells are filled without any winner (tie).

# Code Highlights

Dynamic Button Commands: Each button in the grid is linked to its corresponding row and column through lambda functions.

Random Player Selection: The starting player is chosen randomly using the random module.

Winner Tracking: Winners are appended to the winners.txt file for persistence.
