class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def addStudent(self, roll, name, marks):
        new = Node(roll, name, marks)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        if self.head is None:
            print("No Records")
            return
        temp = self.head
        while temp:
            print("Roll:", temp.roll, "Name:", temp.name, "Marks:", temp.marks)
            temp = temp.next

    def search(self, roll):
        temp = self.head
        while temp:
            if temp.roll == roll:
                print("Record Found -> Roll:", temp.roll, "Name:", temp.name, "Marks:", temp.marks)
                return temp
            temp = temp.next
        print("Record Not Found")
        return None

    def delete(self, roll):
        if self.head is None:
            print("List Empty")
            return
        if self.head.roll == roll:
            self.head = self.head.next
            print("Record Deleted")
            return
        prev = self.head
        temp = self.head.next
        while temp:
            if temp.roll == roll:
                prev.next = temp.next
                print("Record Deleted")
                return
            prev = temp
            temp = temp.next
        print("Record Not Found")

    def update(self, roll, name, marks):
        temp = self.search(roll)
        if temp:
            temp.name = name
            temp.marks = marks
            print("Record Updated")

    def sortByMarks(self):
        if self.head is None:
            return
        temp1 = self.head
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.marks > temp2.marks:
                    temp1.roll, temp2.roll = temp2.roll, temp1.roll
                    temp1.name, temp2.name = temp2.name, temp1.name
                    temp1.marks, temp2.marks = temp2.marks, temp1.marks
                temp2 = temp2.next
            temp1 = temp1.next
        print("Sorted by Marks")
        self.display()

    def sortByRoll(self):
        if self.head is None:
            return
        temp1 = self.head
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.roll > temp2.roll:
                    temp1.roll, temp2.roll = temp2.roll, temp1.roll
                    temp1.name, temp2.name = temp2.name, temp1.name
                    temp1.marks, temp2.marks = temp2.marks, temp1.marks
                temp2 = temp2.next
            temp1 = temp1.next
        print("Sorted by Roll")
        self.display()


obj = StudentList()

while True:
    print("\n1. Add Student")
    print("2. Display Records")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Sort by Marks")
    print("7. Sort by Roll")
    print("8. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        r = int(input("Enter Roll: "))
        n = input("Enter Name: ")
        m = float(input("Enter Marks: "))
        obj.addStudent(r, n, m)
    elif ch == 2:
        obj.display()
    elif ch == 3:
        r = int(input("Enter Roll to Search: "))
        obj.search(r)
    elif ch == 4:
        r = int(input("Enter Roll to Delete: "))
        obj.delete(r)
    elif ch == 5:
        r = int(input("Enter Roll to Update: "))
        n = input("Enter Updated Name: ")
        m = float(input("Enter Updated Marks: "))
        obj.update(r, n, m)
    elif ch == 6:
        obj.sortByMarks()
    elif ch == 7:
        obj.sortByRoll()
    elif ch == 8:
        break
    else:
        print("Invalid Choice")