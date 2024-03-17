import uuid

from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, Enum,
                        Float, ForeignKey, ForeignKeyConstraint, String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class Dog(Base):
    __tablename__ = "dog"
    dog_id = Column(BigInteger, primary_key=True, autoincrement=True)
    birthday = Column(Date)
    weight = Column(Float)
    name = Column(String(5))
    home_id = Column(String(255), ForeignKey("home.home_id"), unique=True)
    img_url = Column(String(255))
    gender = Column(Enum("MALE", "FEMALE"))


class Home(Base):
    __tablename__ = "home"
    home_id = Column(String(255), primary_key=True, default=uuid.uuid4)
    home_name = Column(String(255))
    dog_id = Column(BigInteger, ForeignKey("dog.dog_id"), unique=True)
    dog = relationship(
        "Dog", backref=backref("home", uselist=False), foreign_keys=[dog_id]
    )


class Schedule(Base):
    __tablename__ = "schedules"
    schedule_id = Column(BigInteger, primary_key=True)
    is_active = Column(Boolean, nullable=False)
    is_deleted = Column(Boolean)
    created_date = Column(DateTime(6))
    modified_date = Column(DateTime(6))
    schedule_datetime = Column(DateTime(6), nullable=False)
    home_id = Column(String(255), ForeignKey("home.home_id"), nullable=False)
    memo = Column(Text)
    repeat_id = Column(String(255))
    alert_type = Column(
        Enum("NONE", "ON_TIME", "FIVE_MINUTES", "THIRTY_MINUTES", "ONE_HOUR")
    )
    repeat_type = Column(Enum("NONE", "DAY", "WEEK", "MONTH", "YEAR"))
    schedule_type = Column(
        Enum(
            "WALK",
            "WASH",
            "POO",
            "BRUSH",
            "FOOD",
            "GROOM",
            "HOSPITAL",
            "WATER",
            "ANNIVERSARY",
        ),
        nullable=False,
    )


class User(Base):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    allow_notification = Column(Boolean)
    is_deleted = Column(Boolean)
    dog_id = Column(BigInteger, ForeignKey("dog.dog_id"))
    email = Column(String(255), unique=True)
    home_id = Column(String(255), ForeignKey("home.home_id"))
    img_url = Column(String(255))
    nickname = Column(String(255))
    user_role = Column(Enum("DAD", "MOM", "UNNIE", "OPPA", "NUNA", "HYEONG", "YOUNGER"))
    dog = relationship("Dog", backref="users")
    home = relationship("Home", backref="users")


class ActivityLog(Base):
    __tablename__ = "activity_logs"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_date = Column(DateTime(6))
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    home_id = Column(String(255), ForeignKey("home.home_id"))
    schedule_type = Column(
        Enum(
            "WALK",
            "WASH",
            "POO",
            "BRUSH",
            "FOOD",
            "GROOM",
            "HOSPITAL",
            "WATER",
            "ANNIVERSARY",
        ),
        nullable=False,
    )
    user = relationship("User", backref="activity_logs")
    home = relationship("Home", backref="activity_logs")


class Notification(Base):
    __tablename__ = "notifications"
    notification_id = Column(BigInteger, primary_key=True, autoincrement=True)
    send_date = Column(DateTime(6))
    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    message = Column(String(255))
    notification_type = Column(Enum("SCHEDULE", "SYSTEM"), nullable=False)
    user = relationship("User", backref="notifications")


class UserSchedule(Base):
    __tablename__ = "user_schedules"
    schedule_id = Column(
        BigInteger, ForeignKey("schedules.schedule_id"), primary_key=True
    )
    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    schedule = relationship("Schedule", backref="user_schedules")
    user = relationship("User", backref="user_schedules")


class ScheduleMate(Base):
    __tablename__ = "schedules_mates"
    mates_schedule_id = Column(BigInteger, primary_key=True)
    mates_user_id = Column(BigInteger, primary_key=True)
    schedule_schedule_id = Column(
        BigInteger, ForeignKey("schedules.schedule_id"), nullable=False
    )

    __table_args__ = (
        ForeignKeyConstraint(
            [mates_schedule_id, mates_user_id],
            ["user_schedules.schedule_id", "user_schedules.user_id"],
        ),
    )

    schedule_mate_user = relationship("UserSchedule", backref="schedule_mates_user")
    schedule_mate_schedule = relationship("Schedule", backref="schedule_mates_schedule")
