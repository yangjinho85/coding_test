class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s2:
            self.s1.append(self.s2.pop())
        
        self.s2.append(x)
        
        while self.s1:
            self.s2.append(self.s1.pop())

    def pop(self) -> int:
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s2
        