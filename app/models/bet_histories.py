from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from models.base import Base, session_scope
from models.goal_times import GoalTimes


class BetHistories(Base):
    __tablename__ = 'bet_histories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    league = Column(String(256), nullable=False)
    home_team = Column(String(256), nullable=False)
    away_team = Column(String(256), nullable=False)
    play_time = Column(String(5), nullable=False)
    h_attack = Column(Integer(), nullable=False)
    a_attack = Column(Integer(), nullable=False)
    h_d_attack = Column(Integer(), nullable=False)
    a_d_attack = Column(Integer(), nullable=False)
    h_possession = Column(Integer(), nullable=False)
    a_possession = Column(Integer(), nullable=False)
    h_y_card = Column(Integer(), nullable=False)
    a_y_card = Column(Integer(), nullable=False)
    h_r_card = Column(Integer(), nullable=False)
    a_r_card = Column(Integer(), nullable=False)
    h_corner_kick = Column(Integer(), nullable=False)
    a_corner_kick = Column(Integer(), nullable=False)
    h_on_target = Column(Integer(), nullable=False)
    a_on_target = Column(Integer(), nullable=False)
    h_off_target = Column(Integer(), nullable=False)
    a_off_target = Column(Integer(), nullable=False)
    h_shifts = Column(Integer(), nullable=False)
    a_shifts = Column(Integer(), nullable=False)
    h_pk = Column(Integer(), nullable=False)
    a_pk = Column(Integer(), nullable=False)
    h_goal = Column(Integer(), nullable=False)
    a_goal = Column(Integer(), nullable=False)
    goal_times = relationship('GoalTimes', backref='bet_histories')

    @classmethod
    def create(cls, info):
        history = cls(
            league=info['league'],
            home_team=info['teams'][0],
            away_team=info['teams'][1],
            play_time=info['play_time'],
            h_attack=info['attacks'][0],
            a_attack=info['attacks'][1],
            h_d_attack=info['d_attacks'][0],
            a_d_attack=info['d_attacks'][1],
            h_possession=info['possessions'][0],
            a_possession=info['possessions'][1],
            h_y_card=info['y_card'][0],
            a_y_card=info['y_card'][1],
            h_r_card=info['r_card'][0],
            a_r_card=info['r_card'][1],
            h_corner_kick=info['corner_kick'][0],
            a_corner_kick=info['corner_kick'][1],
            h_on_target=info['on_target'][0],
            a_on_target=info['on_target'][1],
            h_off_target=info['off_target'][0],
            a_off_target=info['off_target'][1],
            h_shifts=info['shifts'][0],
            a_shifts=info['shifts'][1],
            h_pk=info['pk'][0],
            a_pk=info['pk'][1],
            h_goal=info['goals'][0],
            a_goal=info['goals'][1])

        goal_times = []
        if info['goal_times'][0]:
            goal_times += [GoalTimes(time=time, place='home') for time in info['goal_times'][0]]
        if info['goal_times'][1]:
            goal_times += [GoalTimes(time=time, place='away') for time in info['goal_times'][1]]
        if goal_times:
            history.goal_times = goal_times

        with session_scope() as session:
            session.add(history)
