class Library:
    def __init__(self, n):
        self.n = n
        self.borrow = []
    
    def inputData(self):
        for i in range(self.n):
            b = int(input(f"Enter borrow count for book {i+1}: "))
            self.borrow.append(b)

    def averageBorrow(self):
        total = 0
        for i in range(self.n):
            total += self.borrow[i]
        print("Average borrowings =", total / self.n)

    def highestLowest(self):
        max_b = self.borrow[0]
        min_b = self.borrow[0]
        for i in range(self.n):
            if self.borrow[i] > max_b:
                max_b = self.borrow[i]
            if self.borrow[i] < min_b:
                min_b = self.borrow[i]
        print("Highest borrow count =", max_b)
        print("Lowest borrow count =", min_b)

    def countZero(self):
        c = 0
        for i in range(self.n):
            if self.borrow[i] == 0:
                c += 1
        print("Members with 0 borrowings =", c)

    def modeBorrow(self):
        mode = self.borrow[0]
        max_f = 1
        for i in range(self.n):
            f = 1
            for j in range(i+1, self.n):
                if self.borrow[i] == self.borrow[j]:
                    f += 1
            if f > max_f:
                max_f = f
                mode = self.borrow[i]
        print("Most Frequently Borrowed Count =", mode)

n = int(input("Enter number of books: "))
lib = Library(n)
lib.inputData()
lib.averageBorrow()
lib.highestLowest()
lib.countZero()
lib.modeBorrow()
