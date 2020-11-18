# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Paul Mitchell,11/17/2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", 'r')
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task" : strData[0], "Priority" : strData[1]}
    lstTable = [dicRow]
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Your Current Data Is:")
        objFile = open("ToDoList.txt", 'r')
        for row in objFile:
            strData = row.split(",")
            dicRow = {"Task": strData[0], "Priority": strData[1]}
            print(dicRow)
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("\nType in a 'Task' and priority level")
        Task1 = input("Enter a Task: ")
        PriLev1 = input("Enter a Priority Level: ")
        objFile = open("ToDoList.txt", 'a')
        objFile.write(Task1 + "," + PriLev1 + "\n")
        objFile.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strDel = str(input("Which task would you like to delete? "))
        with open("ToDoList.txt", "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if strDel not in line:
                    f.write(line)
            f.truncate()
        print(strDel, "has been deleted")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Data Saved")
        # Additional steps not needed as Menu 2 already saves each new data entry and Menu 3 deletes it
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Program has now completed")
        break  # and Exit the program