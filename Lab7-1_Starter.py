# ------------------------------------------------- #
# Title: Lab7-1 Pickling
# Description: A simple example of storing data in a binary file
# ChangeLog: SMBB, May 31, 2022, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'MyTasks.dat'
to_do_list = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file_name = open('Employee.dat', 'w')
    for row in to_do_list:
        file_name.write(str(row('Employee Name')) + str(row('Employee Role')))
    file_name.close()

def read_data_from_file(file_name):
    file_name = open('Employee', 'r')
    for row in to_do_list:
        file_name.read(str(row('Employee Name')) + str(row('Employee Role')))
    file_name.close()

# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
Employee_Name=str(input('Employee Name:'))
Employee_Role=str(input ('Employee Role:'))
employee_list=[Employee_Name, Employee_Role]
# Storing the list object into a binary file
file_name=open('Employee.dat', 'wb')
pickle.dump(employee_list, file_name)
file_name.close()

# TODO: store the list object into a binary file

# TODO: Read the data from the file into a new list object and display the contents
file_name=open('Employee.dat', 'rb')
file_name_data=pickle.load(file_name)
file_name.close()

print(file_name_data)