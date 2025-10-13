from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship
from db_postgres.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    username = Column(String, nullable=False)
    role = Column(Integer)

    # связи
    statuses = relationship("StatusScheduler", back_populates="user", cascade="all, delete-orphan")
    plans = relationship("PlanSpending", back_populates="user", cascade="all, delete-orphan")
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")
    shares_as_master = relationship("Share", back_populates="master", foreign_keys="Share.master_id", 
                                    cascade="all, delete-orphan")
    shares_as_slave = relationship("Share", back_populates="slave", foreign_keys="Share.slave_id", 
                                   cascade="all, delete-orphan")
    reminders = relationship("Reminders", back_populates="user", cascade="all, delete-orphan")
    
    every_waste = relationship("EveryWaste", back_populates="user", cascade="all, delete-orphan")
    monthly_report = relationship("MonthlyReport", back_populates="user", cascade="all, delete-orphan")

class PlanSpending(Base):
    __tablename__ = "plan_spending"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    category = Column(String, nullable=False)
    amount_money = Column(Integer, nullable=False)

    user = relationship("User", back_populates="plans")
    

class StatusScheduler(Base):
    __tablename__ = "status_scheduler"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    status_notification = Column(Integer)
    status_update = Column(Integer)

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
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    category = Column(String, nullable=False)
    amount_expenses = Column(Integer, nullable=False)

    user = relationship("User", back_populates="expenses")


class Share(Base):
    __tablename__ = "shares"

    id = Column(Integer, primary_key=True, autoincrement=True)
    master_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    slave_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))

    master = relationship("User", back_populates="shares_as_master", foreign_keys=[master_id])
    slave = relationship("User", back_populates="shares_as_slave", foreign_keys=[slave_id])
    
class Reminders(Base):
    __tablename__ = "reminders"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    status = Column(Integer)
    
    user = relationship("User", back_populates="reminders")
    
class EveryWaste(Base):
    __tablename__ = "every_waste"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete="CASCADE"))
    category = Column(String, nullable=False)
    expense = Column(Integer, nullable=False)
    data_time = Column(String)
    comment = Column(String)
    
    user = relationship("User", back_populates="every_waste")
    
class Wishes(Base):
    __tablename__ = "wishes"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger)
    comment = Column(String)
    
class MonthlyReport(Base):
    __tablename__ = "monthly_report"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete="CASCADE"))
    path_to_json = Column(String)
    
    user = relationship("User", back_populates="monthly_report")