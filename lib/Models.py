from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from random import randint

Base = declarative_base()

engine = create_engine('sqlite:///roulette.db')

class Player(Base):
    __tablename__ = "Players"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    balance = Column(Integer())

    games = relationship("Game", back_populates="player")

class Game(Base):
    __tablename__ = "Games"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer, ForeignKey('Players.id'))
    bet_amount = Column(Integer)
    bet_type = Column(String)
    # bet_number = Column(Integer)
    result_number = Column(Integer)
    result_color = Column(String)

    player = relationship("Player", back_populates="games")

    def spin_wheel(self):
        self.result_number = randint(0, 36)
        self.result_color = "Red" if self.result_number % 2 == 0 else "Black"

        return self.result_number, self.result_color
    
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

class RouletteGame:
    __tablename__ = "Roulette Games"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer, ForeignKey('Players.id'))
    bet_amount = Column(Integer)
    bet_type = Column(String)
    bet_number = Column(Integer)
    result_number = Column(Integer)
    result_color = Column(String)

    player = relationship("Player", back_populates="games")

    def spin_wheel(self):
        self.result_number = randint(0, 36)
        self.result_color = "Red" if self.result_number % 2 == 0 else "Black"

        return self.result_number, self.result_color
    
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

