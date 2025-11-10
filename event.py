class EventQueue:
    def __init__(self):
        self.queue = []

    def addEvent(self, event):
        self.queue.append(event)

    def processEvent(self):
        if not self.queue:
            print("No events to process")
        else:
            print("Processed Event:", self.queue.pop(0))

    def displayEvents(self):
        if not self.queue:
            print("No pending events")
        else:
            print("Pending Events:", self.queue)

    def cancelEvent(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print("Event Cancelled:", event)
        else:
            print("Event not found")


obj = EventQueue()

while True:
    print("1. Add an Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        e = input("Enter event name: ")
        obj.addEvent(e)
    elif ch == 2:
        obj.processEvent()
    elif ch == 3:
        obj.displayEvents()
    elif ch == 4:
        e = input("Enter event name to cancel: ")
        obj.cancelEvent(e)
    elif ch == 5:
        break
    else:
        print("Invalid Choice")
