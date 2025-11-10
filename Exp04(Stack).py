class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.document = ""

    def makeChange(self, text):
        self.undo_stack.append(self.document)
        self.document = text
        self.redo_stack = []

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
        else:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
        else:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()

    def display(self):
        print("Current Document State:", self.document)


editor = TextEditor()

while True:
    print("1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        txt = input("Enter new document content: ")
        editor.makeChange(txt)
    elif ch == 2:
        editor.undo()
    elif ch == 3:
        editor.redo()
    elif ch == 4:
        editor.display()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")