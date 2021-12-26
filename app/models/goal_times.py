from sqlalchemy import Column, ForeignKey, Integer, String

from models.base import Base


class GoalTimes(Base):
    __tablename__ = 'goal_times'

    id = Column(Integer, primary_key=True, autoincrement=True)
    bet_history_id = Column(Integer(), ForeignKey('bet_histories.id'))
    place = Column(String(10), nullable=False)
    time = Column(Integer(), nullable=False)
