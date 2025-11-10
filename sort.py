class Salary:
    def __init__(self, n):
        self.n = n
        self.sal = []

    def inputSalary(self):
        for i in range(self.n):
            x = float(input(f"Enter salary {i+1}: "))
            self.sal.append(x)

    def selectionSort(self):
        for i in range(self.n-1):
            for j in range(i+1, self.n):
                if self.sal[i] > self.sal[j]:
                    self.sal[i],self.sal[j] = self.sal[j],self.sal[i]
        print("Salaries after Selection Sort:", self.sal)
        print("Top 5 highest salaries:", self.sal[::-1][:5])

    def bubbleSort(self):
        for i in range(self.n-1):
            for j in range(self.n-1-i):
                if self.sal[j] > self.sal[j+1]:
                    self.sal[j],self.sal[j+1] = self.sal[j+1],self.sal[j]
        print("Salaries after Bubble Sort:", self.sal)
        print("Top 5 highest salaries:", self.sal[::-1][:5])


n = int(input("Enter number of employees: "))
obj = Salary(n)
obj.inputSalary()

print("1. Selection Sort")
print("2. Bubble Sort")
ch = int(input("Enter your choice: "))

if ch == 1:
    obj.selectionSort()
elif ch == 2:
    obj.bubbleSort()
else:
    print("Invalid Choice")
