from utils.openspace import Openspace
from utils.file_utils import open_database

my_file = "./new_colleagues.csv"
names_list= open_database(my_file)
room = Openspace()

room.organize(names_list)

room.display()







