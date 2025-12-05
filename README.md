# HOTELMANAGEMENTSYSTEM-Pythonproject

Author: **Tonny Bett**

## Overview

This project is a Command-Line Interface (CLI) hotel management system built with Python, SQLite, SQLAlchemy ORM, and Alembic migrations. It allows a hotel to manage rooms, guests, and bookings through a simple, interactive terminal interface.

The system demonstrates how to structure a Python project using an ORM, apply database migrations, and create a clean separation between models, business logic, and presentation layers.

## Features

* Add, list, and manage hotel rooms
* Add and manage guests
* Create and track room bookings
* View all data directly from the CLI
* SQLite database for persistence
* SQLAlchemy ORM models for clean data handling
* Alembic migrations for database schema updates
* Seed script for inserting sample data

## Project Structure

```
phase3project/
│
├── lib/
│   ├── cli.py               # CLI menu and user interaction
│   ├── helpers.py           # Helper functions used by the CLI
│   ├── seed.py              # Populate database with sample data
│   ├── debug.py             # Used for debugging models interactively
│   └── db/
│       ├── models.py        # SQLAlchemy ORM models (Room, Guest, Booking)
│       └── __init__.py      # Database engine and session setup
│
├── migrations/              # Alembic migration scripts
│   ├── env.py
│   ├── versions/
│   └── script.py.mako
│
├── alembic.ini              # Alembic configuration
├── hotel.db                 # SQLite database
├── run.py                   # Start the CLI application
├── Pipfile                  # Pipenv dependencies
├── README.md               
```

## Installation

1. Clone the repository:

```
git clone <repository-url>
cd phase3project
```

2. Install dependencies using Pipenv:

```
pipenv install
pipenv shell
```

3. Apply database migrations:

```
alembic upgrade head
```

4. (Optional) Seed the database with sample data:

```
python lib/seed.py
```

## Running the Project

Start the CLI application with:

```
python run.py
```

You will see a menu that allows you to:

* View rooms
* Add rooms
* View guests
* Add guests
* Create bookings
* Exit the program

Each action corresponds to a function in `cli.py`, which interacts with the ORM models.

## Database Models

### Room

Represents a room in the hotel. Includes fields such as id, number, and type.

### Guest

Represents a hotel guest. Contains the guest name and a relationship to bookings.

### Booking

Links a Guest to a Room and stores the booking record.

These models are defined using SQLAlchemy's declarative base.

## Migrations

Alembic is used to manage changes to the database schema over time. When you modify a model, create a migration script:

```
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Debugging

A debug environment is available via:

```
python lib/debug.py
```

This allows testing model queries interactively.

## Seeding Data

To quickly populate the database with predefined rooms, guests, or bookings, run:

```
python lib/seed.py
```

## Contributing

Contributions are welcome. You may open issues or submit pull requests with improvements or bug fixes.

## License

This project is available under an open license. You may modify or distribute it as needed.
