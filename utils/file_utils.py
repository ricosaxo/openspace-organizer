import csv

def open_database (my_file :str) -> list:

    '''
    A Function that returns a list of data from a csv file
    
    parameters:

    my_file(str): a csv file
    
    '''

    names = []
    with open('my_file', mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            names.append(row)
    names = [student for sublist in names for student in sublist] 

    return names

