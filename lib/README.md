# Roulette Game with SQLalchemy

## Overview

This Python project implements a basic Roulette game using SQLalchemy for database management. The game allows players to create accounts, manage balances, and place bets on the Roulette table. The project uses SQLite as the database engine and includes a Command-Line Interface (CLI) for user interaction.

## Instructions for Running the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/roulette-game.git
   cd roulette-game

2. **Install Dependencies:**
    pip install -r requirements.txt

3. **Run the Application:**
    python App.py

Follow the on-screen instructions to navigate through the CLI and interact with the Roulette game.

**Instructions for Using the Project**

**Main Menu**

1. Create Player:

    Enter player name and initial balance to create a new player account.


2. Read Player:

Enter a player ID to view details about a specific player.


3. Update Player Balance

Enter a player ID and the new balance to update a player's balance.

4. Delete Player:

Enter a player ID to delete a player account.

5. Play Roulette:

Enter a player ID to play the Roulette game. Follow on-screen prompts to place bets and spin the wheel.

6. Exit:

Choose this option to exit the program.

**Roulette Gameplay**
Place Your Bet:

Enter the bet amount.

Choose the bet type (red, black, even, odd, or number).
If the bet type is "number," enter a bet number between 1 and 36.

Spinning the Wheel:

Observe the result of the wheel spin, including the number and color.

Payout Calculation:

The game will calculate the payout based on the bet type and number, and update the player's balance accordingly.

Play Again:

Choose whether to play another round or exit.

**Notes**

The project uses SQLite as the database engine, and the database file is named roulette.db.

Make sure to follow the on-screen instructions and enter valid inputs during gameplay.