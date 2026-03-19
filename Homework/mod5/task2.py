class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            raise IndexError("извлечь из пустой очереди")
        val = self.start.data
        if self.start == self.end:
            self.start = None
            self.end = None
        else:
            self.start = self.start.nref
            self.start.pref = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        if n < 0:
            raise IndexError("index не в диапозоне")
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            if self.start:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        index = 0
        while current is not None and index < n - 1:
            current = current.nref
            index += 1

        if current is None:
            raise IndexError("index не в диапозоне")

        new_node = Node(val)
        new_node.nref = current.nref
        new_node.pref = current
        if current.nref:
            current.nref.pref = new_node
        current.nref = new_node
        if current == self.end:
            self.end = new_node

    def print(self):
        current = self.start
        values = []
        while current is not None:
            values.append(current.data)
            current = current.nref
        if values:
            print(" ".join(map(str, values)))
        else:
            print("Очередь пуста")