# Define a function to read the list of todos from the file
def getTodos(filepath="todos.txt"):
    with open("todos.txt", "r") as file: # Open file in read mode
                todos = file.readlines() # Read all lines into a list
    return todos # Return that list to the caller

# Define a function to save the list of todos back to the file
def write_todos(todos_arg , filepath="todos.txt"):
    with open(filepath , "w") as file: # Open file in write mode (overwrites)
        file.writelines(todos_arg) # Write the entire list to the file

if __name__ == "__main__":
      print("hello")
      print(getTodos())