from sqlalchemy.orm import Session
from Models import Player, Game, engine, Base
from Seeds import create_player, read_player, update_player_balance, delete_player, seed_data

def create_game(session, player, bet_amount, bet_type, bet_number=None):
    game = Game(player=player, bet_amount=bet_amount, bet_type=bet_type, bet_number=bet_number)
    session.add(game)
    session.commit()
    return game

def spin_wheel(game):
    result_number, result_color = game.spin_wheel()
    print(f"Result: Number - {result_number}, Color - {result_color}")
    return result_number, result_color

def calculate_payout(self):
    if self.bet_type == "color":      
            if self.result_color == self.bet_number:
                payout_ratio = 2  
                winnings = self.bet_amount * payout_ratio
                self.player.balance += winnings
                print(f"Congratulations! You won {winnings} chips :).")
            else:
                print("Sorry, you lost :(.")
    elif self.bet_type == "number":
        if self.result_number == self.bet_number:
            payout_ratio = 36  
            winnings = self.bet_amount * payout_ratio
            self.player.balance += winnings
            print(f"Congratulations! You won {winnings} chips.")
        else:
            print("Oh no!! You lost </3.")

    else:
        print("Invalid bet type :( no payout calculated.")

def main():
    Base.metadata.create_all(engine)

    seed_data()

    while True:
        print("1. Create Player")
        print("2. Read Player")
        print("3. Update Player Balance")
        print("4. Delete Player")
        print("5. Create Game")
        print("6. Spin Wheel")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter player name: ")
            balance = int(input("Enter initial balance: "))
            with Session(engine) as session:
                create_player(session, name, balance)
            print("Welcome New Player!!!")

        elif choice == "2":
            player_id = int(input("Enter player ID: "))
            with Session(engine) as session:
                player = read_player(session, player_id)
                if player:
                    print(f"Player ID: {player.id}, Name: {player.name}, Balance: {player.balance}")
                else:
                    print("Player not found.")

        elif choice == "3":
            player_id = int(input("Enter player ID: "))
            new_balance = int(input("Enter new balance: "))
            with Session(engine) as session:
                player = update_player_balance(session, player_id, new_balance)
                if player:
                    print(f"Balance updated successfully. New balance: {player.balance}")
                else:
                    print("Player not found.")

        elif choice == "4":
            player_id = int(input("Enter player ID: "))
            with Session(engine) as session:
                delete_player(session, player_id)
                print("Player deleted successfully.")

        elif choice == "5":
            player_id = int(input("Enter player ID: "))
            bet_amount = int(input("Enter bet amount: "))
            bet_type = input("Enter bet type (e.g., color, number): ")
            bet_number = int(input("Enter bet number (if applicable): "))
            with Session(engine) as session:
                player = read_player(session, player_id)
                if player:
                    create_game(session, player, bet_amount, bet_type, bet_number)
                    print("Game created successfully.")
                else:
                    print("Player not found.")

        elif choice == "6":
            game_id = int(input("Enter game ID: "))
            with Session(engine) as session:
                game = session.query(Game).get(game_id)
                if game:
                    spin_wheel(game)
                    calculate_payout(game)
                else:
                    print("Game not found.")

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
