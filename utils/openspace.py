import csv
import random as rd
from file_utils import open_database
from table import Table,Seat


class Openspace(Table):

    # Taking a list of students from the csv file
    names = open_database("new_colleagues.csv")


    '''
    A class representing the Openspace

        Attributes:

        number_of_tables(int): The number of tables in the openspace (default = 6)
        tables(list): A list of all the Table ojects
    
    '''

    def __init__ (self, number_of_tables = 6):
        self.number_of_tables = number_of_tables
        self.tables = []
            

    def organize(names :list):
        
        '''
        The method that assigns people to `Seat` objects in the different `Table` objects
        
        parameter:

        name(list): list of the seat objects to put in table seat
        '''

        #Shuffle the list before assigning it

        rd.shuffle(names)

        # Assigning the students to the seats and populating a list with seat objects
        list_of_seats = []
        
        for name in names:
            seat = Seat()
            seat.set_occupant(name)
            list_of_seats.append(seat) 

        # Initializing the table objects and populating the self.tables with table objects
        
        for _ in range(self.number_of_tables):
            table = Table()
            self.tables.append(table)
        
        # Start to assign the seat objects to the table objects
        seat_index = 0
        while seat_index < len(list_of_seats):
            for table in self.tables:
                if seat_index < len(list_of_seats) and table.has_free_spot():
                    table.seats.append(list_of_seats[seat_index])
                    seat_index += 1
                else:
                    break

     

    def display(self):
        
        '''The method that display the different tables and there occupants in a nice and readable way'''
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                print(f"  - {seat.occupant}")
        else:
            print(" - No occupants") 
       
    

    def store(filename :str):
        
        '''
        The method that stores the repartition in an excel file

        parameter:

        filename(str): name of file to store in
        
        '''
        with open(filename, 'w') as file:
             writer = csv.writer(file)
             writer.writerows()
   
    
    def __str__(self) -> str:

        "The method returns a human-readable, or informal, string representation of an object"
        