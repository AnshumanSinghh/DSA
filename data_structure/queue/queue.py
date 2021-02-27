# Queue implementation in Python
"""
The complexity of enqueue and dequeue operations in a queue using an array is O(1).
"""

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    
    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1: # check if queue is empty
            return None
        print("popped:", self.queue[0])
        return self.queue.pop(0)  # delete the first element always


    # Display the queue
    def display(self):
        print(self.queue)

    # To get the length of the queue
    def size(self):
        return len(self.queue)

# Driver Code Starts
if __name__ == "__main__":
    q = Queue()  # object creation

    # now calling methods using object
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("After 5 enqueue:", q.size())
    
    q.enqueue(6)

    q.display()

    q.dequeue()
    q.dequeue()

    q.display()
    print("At end:", q.size())
