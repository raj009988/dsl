class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hashFunction(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hashFunction(key)
        start = index
        while self.table[index] is not None and self.table[index] != "DELETED":
            index = (index + 1) % self.size
            if index == start:
                print("Hash Table is Full")
                return
        self.table[index] = key
        print("Key Inserted")

    def search(self, key):
        index = self.hashFunction(key)
        start = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print("Key Found at Index", index)
                return
            index = (index + 1) % self.size
            if index == start:
                break
        print("Key Not Found")

    def delete(self, key):
        index = self.hashFunction(key)
        start = index
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = "DELETED"
                print("Key Deleted")
                return
            index = (index + 1) % self.size
            if index == start:
                break
        print("Key Not Found")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


obj = HashTable()

while True:
    print("1. Insert Key")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Table")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        k = int(input("Enter Key: "))
        obj.insert(k)
    elif ch == 2:
        k = int(input("Enter Key to Search: "))
        obj.search(k)
    elif ch == 3:
        k = int(input("Enter Key to Delete: "))
        obj.delete(k)
    elif ch == 4:
        obj.display()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")
