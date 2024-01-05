from sqlalchemy.orm import Session
from Models import Player, Game, engine, Base

Base.metadata.create_all(engine)

def create_player(session, name, balance):
    player = Player(name=name, balance=balance)
    session.add(player)
    session.commit()
    return player

def read_player(session, player_id):
    return session.query(Player).get(player_id)

def update_player_balance(session, player_id, new_balance):
    player = session.query(Player).get(player_id)
    player.balance = new_balance
    session.commit()
    return player

def delete_player(session, player_id):
    player = session.query(Player).get(player_id)
    session.delete(player)
    session.commit()

def seed_data():
    with Session(engine) as session:
        pass

def create_game(session, user_id, bet_amount, bet_type, result_number, result_color):
    game = Game(user_id=user_id, bet_amount=bet_amount, bet_type=bet_type, result_number=result_number, result_color=result_color)
    session.add(game)
    session.commit()
    return game

if __name__ == "__main__":
    
    seed_data()
