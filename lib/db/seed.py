from models import Room, Guest, Staff, session
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Create 5 rooms
for i in range(101, 106):
    room = Room(number=i, type="Single", price=100)
    session.add(room)

# Create 5 guests
for _ in range(5):
    guest = Guest(name=fake.name(), phone=fake.phone_number(), email=fake.email())
    session.add(guest)

# Create 3 staff members
staff_roles = ["Receptionist", "Manager", "Cleaner"]
for role in staff_roles:
    staff = Staff(name=fake.name(), role=role, shift="Day")
    session.add(staff)

session.commit()
print("Database seeded successfully!")
