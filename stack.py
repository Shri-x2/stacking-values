class Stack():
    def __init__(self, n):
        self.stack = []
        self.n = n
    def push(self, value):
        if self.n > len(self.stack):
            self.stack.append(value)
        else:
            print("Overflow")

    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
        else:
            print("Underflow")

    def top(self):
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print("Empty stack")

    def display(self):
        print(self.stack)

    def size(self):
        print(self.n)

    def availability(self):
        print(self.n - len(self.stack))

s = Stack(4)
s.push(5)
s.push(7)
s.display()
s.availability()
s.push(3)
s.display()
s.availability()
s.push(8)
s.display()
s.availability()
s.push(2)
s.display()
s.availability()
for i in range(5):
    s.pop()
    s.display()
    s.availability()