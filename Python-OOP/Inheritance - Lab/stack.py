from typing import List


class Stack:
    def __init__(self):
        self.data: List = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[len(self.data) - 1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        self.data.reverse()

        return f"[{', '.join(self.data)}]"
      
