from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    number = Column(String)
    type = Column(String)
    bookings = relationship("Booking", back_populates="room")

class Guest(Base):
    __tablename__ = "guests"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bookings = relationship("Booking", back_populates="guest")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey("guests.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    guest = relationship("Guest", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")

class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
