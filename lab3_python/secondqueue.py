import json
class Queue:
    queues = {}

    @classmethod
    def save(cls, filename):
        with open(filename, 'w') as file:
            queue_list = []
            for name, queue in cls.queues.items():
                queue_data = {'name': queue.name, 'size': queue.size, 'items': queue.items}
                queue_list.append(queue_data)
            json.dump(queue_list, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            queue_list = json.load(file)
            for queue_data in queue_list:
                name = queue_data['name']
                size = queue_data['size']
                items = queue_data['items']
                cls.queues[name] = cls(name, size)
                cls.queues[name].items = items

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = []
        self.__class__.queues[name] = self

    def insert(self, value):
        if len(self.items) < self.size:
            self.items.append(value)
        else:
            raise QueueOutOfRangeException("Queue size exceeded")

    def pop(self):
        if self.is_empty():
            print("empty queue")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class QueueOutOfRangeException(Exception):
    def __init__(self, message="Queue size exceeded"):
        self.message = message
        super().__init__(self.message)
q1 = Queue("queue1", 3)
q1.insert(4)
q1.insert(2)
q1.insert(3)
# q1.insert(4)

q2 = Queue("queue2", 3)
q2.insert(40)
q2.insert(20)
q2.insert(30)

Queue.save("queues.json")
Queue.load("queues.json")

q_loaded = Queue.queues["queue1"]
print(q_loaded.pop())
q_loaded = Queue.queues["queue2"]
print(q_loaded.pop())

# ////////////////////////////////////////////////////////
class QueueWithAttributes:
    all_queues = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.items = []

        if self.name in self.all_queues:
            raise ValueError("Queue with this name already exists.")
        else:
            self.all_queues[self.name] = self

    def insert(self, value):
        "Inserts a new value at the rear of the queue."
        if len(self.items) < self.size:
            self.items.append(value)
        else:
            raise QueueOutOfRangeException("Queue size exceeded.")

    def pop(self):
        "Returns and removes a value from the front of the queue."
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("empty queue")
            return None

    def is_empty(self):
        return len(self.items) == 0

    @classmethod
    def get_queue_by_name(cls, name):
        "Returns a queue instance by its name."
        return cls.all_queues.get(name)

class QueueOutOfRangeException(Exception):
    pass
try:
    q1 = QueueWithAttributes(name="queue1", size=2)
    q1.insert(1)
    q1.insert(2)
    q1.insert(3)  # Raises QueueOutOfRangeException

    q2 = QueueWithAttributes(name="queue2", size=1)
    q2.insert(1)
    q2.insert(2)  # Raises QueueOutOfRangeException

    q3 = QueueWithAttributes.get_queue_by_name("queue1")
    print(q3.pop())  # Output: 1
except QueueOutOfRangeException as e:
    print(f"Exception: {e}")