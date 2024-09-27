


class Seat():
    
    '''
        A class representing a seat
        
        Attributes:
        
        free(bool): Is the seat still available?
        occupant(str): Assign the seat to someone 
    '''

    def __init__(self, free = True, occupant = ""):

        """
        Constructs a Seat object.

        Parameters:
            free(bool): True when seat is available
            occupant(str): Assign the seat to someone 
        """

    
        self.free = free
        self.occupant = occupant
        
    
    
    def set_occupant(self, name):

        """
        The method to add someone to a Seat object.

        Parameters:
            name (str): The name to be added.

        """


        self.free = False
        self.occupant = name
        



    def remove_occupant(self):
        
        '''The method to remove someone from a Seat object.'''
        
        self.free = True
        self.occupant = ""
        

    def __str__(self) -> str:

        "The method returns a human-readable, or informal, string representation of an object"
        
        if self.free == True:
            return f'This a seat object taken by {self.occupant}'
        return f'This seat object is still free'







class Table:

    '''
    A class representing a table

        Attributes:

        capacity(int): The number of seats available
        seats (list): list of taken seats at the table
        free(bool): shows if there is a free seats available

    '''
    
    
    def __init__(self, capacity = 4):

        '''
        
        Constructs a Seat object.

        Parameter:

        capacity(int): the number of seats at the table (default = 4)
        
        
        '''
       
        self.capacity = capacity
        self.seats = []
       


    def has_free_spot(self) -> bool:
       
        '''The method that returns the boolean True if a spot is available'''
       
        if len(self.seats) < self.capacity:
             self.free = True
        

    def assign_seat(self, name :str):
        
        '''
        The method that places someone at the table

        parameter:

        name(str): the seat object to put in table seat

        '''
        seat = Seat()
        seat.set_occupant(name)
        self.seats.append(seat)

        

    def left_capacity(self) -> int:

        '''The method that returns an integer representing the number of available free seats'''
       
        return len(self.seats) - self.capacity
        

    def __str__(self) -> str:

        "The method returns a human-readable, or informal, string representation of an object"
        
        return f'This gives a table object with {self.capacity} left and {self.seats} taken'



