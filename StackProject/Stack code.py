1"""
for stack, we make:
A pop function
A push function
An initialise function
and a display function
"""
stack = [None for i in range(6)]
np = -1
tp = np

def initialiseStack():
    global tp, np
    tp = np
    for i in range(6):
        stack[i] = None

def push(data):
    global tp
    if tp == len(stack)-1:
        print("stack is full")
    else:
        tp = tp + 1
        stack[tp] = data

def pop():
    global tp
    if tp == np:
        print("stack is already empty")
    else:
        data = stack[tp]
        stack[tp] = None
        tp = tp - 1
    return data

def display():
    for i in range(len(stack)-1,-1,-1):
        if i == tp:
            print(stack[i],"<--top")
        else:
            print(stack[i])

# main program
def menu(choice):
   choice = 0
   while choice != 5:
       choice = int(input("Enter your choice (1 - 5) : "))
       if choice == 1:
          data = input("Enter data to push into stack : ")
          push(data)
       elif choice == 2:
           data = pop()
           if data != None:
               print("Data popped = ", data)
       elif choice == 3:
           display()
       elif choice == 4:
         initialiseStack()
         print("Stack initialized.")
       elif choice == 5:
           print("Exiting...")
       else:
           print("Invalid choice. Please try again.")
# end of while loop and end of program

choice = input()
menu(choice)
