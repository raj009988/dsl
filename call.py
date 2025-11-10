class CallCenter:
    def __init__(self):
        self.queue = []

    def addCall(self, customerID, callTime):
        self.queue.append([customerID, callTime])

    def answerCall(self):
        if not self.queue:
            print("No calls to answer")
        else:
            print("Answered Call:", self.queue.pop(0))

    def viewQueue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Current Call Queue:")
            for call in self.queue:
                print("Customer:", call[0], ", Call Time:", call[1])

    def isQueueEmpty(self):
        if not self.queue:
            print("Queue is Empty")
        else:
            print("Queue is Not Empty")


obj = CallCenter()

while True:
    print("\n1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        cid = input("Enter Customer ID: ")
        ctime = input("Enter Call Time (minutes): ")
        obj.addCall(cid, ctime)
    elif ch == 2:
        obj.answerCall()
    elif ch == 3:
        obj.viewQueue()
    elif ch == 4:
        obj.isQueueEmpty()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")
