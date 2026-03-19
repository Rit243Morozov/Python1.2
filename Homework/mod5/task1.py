class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            raise IndexError("извлечь из пустого стека")
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        current = self.end
        values = []
        while current is not None:
            values.append(current.data)
            current = current.pref
        if values:
            print(" ".join(map(str, reversed(values))))
        else:
            print("Стек пуст")