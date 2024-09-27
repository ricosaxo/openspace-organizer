import csv
import random as rd
from file_utils import open_database
from table import Table


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
        super().__init__()

        pass

    def organize(names :list):
        
        '''
        The method that assigns people to `Seat` objects in the different `Table` objects
        
        parameter:

        name(list): list of the seat objects to put in table seat
        '''

        #Shuffle the list before assigning it

        rd.shuffle(names)




        pass

    def display(self):
        
        '''The method that display the different tables and there occupants in a nice and readable way'''
        pass

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
        pass