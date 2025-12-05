from db.models import Room, Guest, Booking, session

# Test query examples
print("All Rooms:")
print(session.query(Room).all())

print("All Guests:")
print(session.query(Guest).all())
