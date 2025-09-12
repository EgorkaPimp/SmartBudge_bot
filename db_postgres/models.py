from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    role = Column(Integer)

    # связи
    statuses = relationship("StatusScheduler", back_populates="user")
    plans = relationship("PlanSpending", back_populates="user")
    expenses = relationship("Expense", back_populates="user")
    shares_as_master = relationship("Share", back_populates="master", foreign_keys="Share.master_id")
    shares_as_slave = relationship("Share", back_populates="slave", foreign_keys="Share.slave_id")

class PlanSpending(Base):
    __tablename__ = "plan_spending"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String, nullable=False)
    amount_money = Column(Integer, nullable=False)

    user = relationship("User", back_populates="plans")
    

class StatusScheduler(Base):
    __tablename__ = "status_scheduler"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Integer)

    user = relationship("User", back_populates="statuses")
    
class SchedulerDefault(Base):
    __tablename__ = "scheduler_default"

    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    hour = Column(Integer)
    minute = Column(Integer)
    
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String, nullable=False)
    amount_expenses = Column(Integer, nullable=False)

    user = relationship("User", back_populates="expenses")


class Share(Base):
    __tablename__ = "shares"

    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, ForeignKey("users.id"))
    slave_id = Column(Integer, ForeignKey("users.id"))

    master = relationship("User", back_populates="shares_as_master", foreign_keys=[master_id])
    slave = relationship("User", back_populates="shares_as_slave", foreign_keys=[slave_id])