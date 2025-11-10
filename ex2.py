class ECommerce:
    def __init__(self, n):
        self.n = n
        self.acc = []

    def inputIDs(self):
        for i in range(self.n):
            x = int(input(f"Enter Account ID {i+1}: "))
            self.acc.append(x)

    def linearSearch(self, key):
        for i in range(self.n):
            if self.acc[i] == key:
                return i
        return -1

    def binarySearch(self, key):
        l = 0
        r = self.n - 1
        while l <= r:
            mid = (l + r) // 2
            if self.acc[mid] == key:
                return mid
            elif self.acc[mid] < key:
                l = mid + 1
            else:
                r = mid - 1
        return -1


n = int(input("Enter number of Account IDs: "))
obj = ECommerce(n)
obj.inputIDs()

key = int(input("Enter Account ID to search: "))

print("1. Linear Search")
print("2. Binary Search")
choice = int(input("Enter your choice: "))

if choice == 1:
    pos = obj.linearSearch(key)
    if pos != -1:
        print("Account ID found at position", pos+1)
    else:
        print("Account ID not found")

elif choice == 2:
    print("Sorted Account IDs:", obj.acc)
    pos = obj.binarySearch(key)
    if pos != -1:
        print("Account ID found in sorted list at position", pos+1)
    else:
        print("Account ID not found")

else:
    print("Invalid Choice")
