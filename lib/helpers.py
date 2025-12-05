from db.models import Room, Guest, Booking, Staff, session
from datetime import datetime

# Rooms
def list_rooms():
    rooms = session.query(Room).all()
    for r in rooms:
        print(f"Room {r.number} | Type: {r.type} | Price: ${r.price} | Available: {r.is_available}")

def create_room():
    number = int(input("Enter room number: "))
    type_ = input("Enter room type (Single/Double/Suite): ")
    price = float(input("Enter room price: "))
    room = Room(number=number, type=type_, price=price)
    session.add(room)
    session.commit()
    print("Room created successfully!")

# Guests
def list_guests():
    guests = session.query(Guest).all()
    for g in guests:
        print(f"Guest {g.id} | Name: {g.name} | Phone: {g.phone} | Email: {g.email}")

def create_guest():
    name = input("Enter guest name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    guest = Guest(name=name, phone=phone, email=email)
    session.add(guest)
    session.commit()
    print("Guest added successfully!")

# Bookings
def create_booking():
    list_guests()
    guest_id = int(input("Enter guest ID: "))
    list_rooms()
    room_id = int(input("Enter room ID: "))
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")
    booking = Booking(guest_id=guest_id, room_id=room_id,
                      check_in=datetime.strptime(check_in, "%Y-%m-%d"),
                      check_out=datetime.strptime(check_out, "%Y-%m-%d"))
    # Mark room unavailable
    room = session.query(Room).get(room_id)
    room.is_available = False
    session.add(booking)
    session.commit()
    print("Booking created successfully!")

def list_bookings():
    bookings = session.query(Booking).all()
    for b in bookings:
        print(f"Booking {b.id} | Guest: {b.guest.name} | Room: {b.room.number} | "
              f"Check-in: {b.check_in} | Check-out: {b.check_out}")

# Available rooms
def available_rooms():
    rooms = session.query(Room).filter_by(is_available=True).all()
    for r in rooms:
        print(f"Room {r.number} | Type: {r.type} | Price: ${r.price}")

# Staff
def list_staff():
    staff_members = session.query(Staff).all()
    for s in staff_members:
        print(f"Staff {s.id} | Name: {s.name} | Role: {s.role} | Shift: {s.shift}")
