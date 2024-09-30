Openspace Seating Organizer

Project Description

This project implements an Openspace seating organizer system. It allows for the automatic assignment of students or participants to seats at different tables within an open space environment. The system is designed to be flexible, allowing for various configurations of tables and seats.

Features

Create and manage Seat objects
Create and manage Table objects with multiple seats
Create an Openspace with multiple tables
Randomly assign participants to seats
Display seating arrangements
Store seating arrangements in a CSV file

Classes

Seat

Represents an individual seat with attributes:

free: Boolean indicating if the seat is available
occupant: String representing the name of the seat occupant

Table

Represents a table with attributes:

capacity: Integer indicating the number of seats at the table
seats: List of Seat objects assigned to the table

Openspace

Represents the entire open space area with attributes:

number_of_tables: Integer indicating the number of tables in the space

tables: List of Table objects in the open space

Usage

Import the necessary classes:

from utils.table import Table, Seat
from openspace import Openspace

Create an Openspace object:

openspace = Openspace(number_of_tables=6)

Load participant names from a CSV file:

names = open_database('participants.csv')

Organize the seating:

openspace.organize(names)

Display the seating arrangement:

openspace.display()

Store the seating arrangement in a CSV file:

openspace.store('seating_arrangement.csv')

Installation

Clone this repository
Ensure you have Python 3.x installed

Install required dependencies (if any) using:
pip install -r requirements.txt
