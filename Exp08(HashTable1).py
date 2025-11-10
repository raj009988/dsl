class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hashFunction(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hashFunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hashFunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print("Key Found -> Value:", pair[1])
                return
        print("Key Not Found")

    def delete(self, key):
        index = self.hashFunction(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print("Key Deleted")
                return
        print("Key Not Found")

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


obj = HashTable()

while True:
    print("1. Insert Key-Value")
    print("2. Search Key")
    print("3. Delete Key")
    print("4. Display Table")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        k = int(input("Enter Key: "))
        v = input("Enter Value: ")
        obj.insert(k, v)
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