from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from random import randint

Base = declarative_base()

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
    bet_number = Column(Integer)
    result_number = Column(Integer)
    result_color = Column(String)

    player = relationship("Player", back_populates="games")

engine = create_engine('sqlite:///roulette.db')
Base.metadata.create_all(engine)

class RouletteGame:
    def __init__(self, player, bet_amount, bet_type, bet_number=None):
        self.player = player
        self.bet_amount = bet_amount
        self.bet_type = bet_type
        self.bet_number = bet_number
        self.result_number = None
        self.result_color = None

    def spin_wheel(self):
        self.result_number = randint(0, 36)
        self.result_color = "Red" if self.result_number % 2 == 0 else "Black"

        return self.result_number, self.result_color
    
    def calculate_payout(self):
        pass