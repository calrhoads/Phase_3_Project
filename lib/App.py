from sqlalchemy.orm import Session
from Models import *
from Seeds import create_player, read_player, update_player_balance, delete_player, seed_data

def create_game(session, player, bet_amount, bet_type, bet_number=None):
    roulette_game = Game(player=player, bet_amount=bet_amount, bet_type=bet_type, bet_number=bet_number)
    session.add(roulette_game)
    session.commit()
    return roulette_game

def spin_wheel(roulette_game):
    result_number, result_color = roulette_game.spin_wheel()
    print(f"Result: Number - {result_number}, Color - {result_color}")
    return result_number, result_color

def play_roulette(session, player):
    print("Welcome to the Roulette Table!")
    while True:
        print("\nPlace your bet:")
        bet_amount = int(input("Enter bet amount: "))
        bet_type = input("Enter bet type (red, black, even, odd, number): ")

        if bet_type.lower() == "number":
            bet_number = int(input("Enter bet number (1-36): "))
        else:
            bet_number = None

        roulette_game = create_game(session, player, bet_amount, bet_type, bet_number)

        print("\nSpinning the wheel...")
        result_number, result_color = spin_wheel(roulette_game)
        print(f"Result: Number - {result_number}, Color - {result_color}")
        roulette_game.calculate_payout()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Exiting the roulette table.")
            break


def main():
    Base.metadata.create_all(engine)

    seed_data()

    while True:
        print("1. Create Player")
        print("2. Read Player")
        print("3. Update Player Balance")
        print("4. Delete Player")
        print("5. Play Roulette")
        print("6. Exit")

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
            with Session(engine) as session:
                player = read_player(session, player_id)
                if player:
                    play_roulette(session, player)
                else:
                    print("Player not found.")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()