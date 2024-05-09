class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("empty queue")
            return None

    def is_empty(self):
        return len(self.items) == 0

q = Queue()
q.insert(1)
q.insert(2)
print(q.pop())  
print(q.pop())  
print(q.is_empty())  