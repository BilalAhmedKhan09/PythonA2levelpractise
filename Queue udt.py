
class saledata:
    def _init_(self) :
        self.id = " "
        self.quantity = 0
queue = [saledata() for i in range(5)]
numberofitems = 0
tail = 0
head = 0
def init():
    global tail, head, numberofitems, queue
    for i in range(5):
        queue[i].id = " "
        queue[i].quantity = -1
        head = 0
        tail = 0
        numberofitems = 0
    print("Initialised")
def enqueue(data):
    global tail, head, queue, numberofitems
    if numberofitems == len(queue):
        return -1
    elif head == len(queue):
         head = 0
    else:
      head = head + 1
    queue[head] = data
    numberofitems = numberofitems + 1
    print(numberofitems)
    return 1
def dequeue():
    global queue, numberofitems, tail
    data = saledata()
    data.id = " "
    data.quantity = -1
    if numberofitems == 0:
        print("queue is empty")
    elif tail == len(queue) - 1:
         tail = 0
    else:
        tail = tail + 1
    queue[tail].id = data.id
    queue[tail].quantity = data.quantity
    numberofitems -= 1

def enterrecord():
    tdata = saledata()
    tdata.id = input("Enter id:")
    tdata.quantity = input("Enter quantity:")
    saledata.id = tdata.id
    saledata.quantity = tdata.quantity
    reply = enqueue(tdata)
    if reply == -1:
        print("queue is full")
    elif reply == 1:
        print("Stored")
def m():
    choice = 0
    while choice != 5:
        choice = int(input("enter choice"))
        if choice == 1:
            init()
        elif choice == 2:
            enterrecord()
        elif choice == 3:
             dequeue()
        else:
            print("ID   Quantity")
            for i in range(5):
                print(queue[i].id,"  ",queue[i].quantity)


m()