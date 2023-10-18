#this is the python code for a basic queue
queue = [None for i in range(5)]
np = 0
tp = np
hp = np
size = 0
def enqueue(data):
    global queue, np, tp, hp, size
    if size == len(queue):
     print("queue is full")
    elif hp == len(queue) - 1:
        hp == 1
    else:
        tp = tp + 1
        hp = hp + 1
    queue[hp] = data
    size = size + 1
def dequeue():
    global queue, tp, hp, np, size
    remove = " "
    queue[tp] = remove
    if size == 0:
        print("queue is empty")
    elif tp == len(queue) - 1:
         tp = 0
    else:
        tp = tp + 1
    queue[tp] == None
    size = size - 1
    return remove
def init():
    global tp, hp, size, queue, np
    queue = [None for i in range(5)]
    tp = np
    hp = np
    size = 0
    print("initialised")
input(choice)
while choice != 5:
      if choice == 1:
          init()
      elif choice == 2:
         data = input()
         enqueue(data)
      else:
          dequeue()

















