# Deque [Doubly Ended Queue] implementation with Python

class Deque():
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        return self.items.append(item)
    
    def addFront(self, item):
        return self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop()

    def removeFront(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# Driver Code Starts
if __name__ == "__main__":
    d = Deque()
    print("Is Deque is empty?", d.isEmpty())
    
    d.addRear(8)
    d.addRear(5)
    d.addFront(7)
    d.addFront(10)
    print("After first four insertions:",d.items, "\n")

    print("length of the Dequeue is:", d.size())
    print("Is Deque is empty?", d.isEmpty())
    d.addRear(11)
    print("After one more insertion(11):", d.items, "\n")

    print(d.removeRear(), "is removed from Rear.")
    print(d.removeFront(), "is removed from Front.")
    print("After removal from Rear and Front:", d.items)
    
    d.addFront(55)
    d.addRear(45)
    print(d.items)
