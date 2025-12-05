import click
from lib.helpers import (
    list_rooms,
    create_room,
    list_guests,
    create_guest,
    create_booking,
    list_bookings,
    available_rooms,
    list_staff,
)

@click.group()
def cli():
    """Welcome to the Hotel Management System CLI"""
    pass

# Rooms
@cli.command()
def rooms():
    list_rooms()

@cli.command()
def create_room_cmd():
    create_room()

# Guests
@cli.command()
def guests():
    list_guests()

@cli.command()
def create_guest_cmd():
    create_guest()

# Bookings
@cli.command()
def book_room():
    create_booking()

@cli.command()
def bookings():
    list_bookings()

# Availability
@cli.command()
def available():
    available_rooms()

# Staff
@cli.command()
def staff():
    list_staff()

if __name__ == "__main__":
    cli()
def main():
    print("=== HOTEL MANAGEMENT SYSTEM ===")
    print("System is running correctly!")
