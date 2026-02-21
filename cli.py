import os  # Import the OS module to check for file existence

# Check if the data file exists; if not, create an empty one
if not os.path.exists("todos.txt"):
    open("todos.txt","w").close()

from function import getTodos , write_todos  # type: ignore #importing the file named function

import time

now = time.strftime("%b %d ,%Y %H:%M:%S")
print("its now" , now)

# Start an infinite loop to keep the program running
while True:
    # Prompt user for input and remove leading/trailing whitespace
    user_input = (input("Type add ,show ,exit ,edit or complete: ")).strip()
    
    # Check if the user wants to add a new item
    if user_input.startswith("add"):
        try:
            added_todo = user_input[4:] + "\n" # Extract task text and add a newline
            
            todos = getTodos() # Load current list from file

            todos.append(added_todo) # Add the new task to the list

            write_todos(todos) # Save the updated list back to the file
        except(ValueError): # Catch input errors
            continue

    # Check if the user wants to view the list            
    elif user_input.startswith("show"):
        try:
            todos = getTodos() # Load current list

            print("your todos are listed below.")    

            # Create a new list with newline characters removed for clean printing
            new_todos = [item.strip('\n') for item in todos]

            # Loop through the list to print items with their numbers (starting at 1)
            for index ,items in enumerate(new_todos):
                row = f"{index+1}.{items}" 
                print(row)
        except(ValueError):
            continue

    # Check if the user wants to modify an existing item
    elif user_input.startswith("edit"):
        try:    
            print("ohh! you want to edit your todo.")
            # Convert user string number to integer index (e.g., "1" becomes 0)
            number = int(user_input[5:]) - 1
            todos = getTodos() # Load current list
            user_action = input("Enter your edited todo:") # Get new text
            
            todos[number]= user_action + '\n' # Replace old item at specific index
            write_todos(todos) # Save changes
        except(ValueError):
            continue
        
    # Check if the user wants to mark an item as done (remove it)
    elif user_input.startswith("complete"):
        try:
            # Convert user string number to integer index
            number = int(user_input[9:]) - 1
            todos = getTodos() # Load current list
            print("ok, removing todo from todo list.")
            todos.pop(number) # Remove the item at the specified index

            write_todos(todos) # Save updated list
        except(ValueError):
            continue
        
    # Check if the user wants to close the program
    elif "exit" in user_input:
        break # Break the infinite loop
    else:
        break # Break if any other command is entered (optional logic)

# Final message printed after the loop ends
print("Your code has been ran sucsecsfully.")

