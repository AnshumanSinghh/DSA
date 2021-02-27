# Circular Queue implementation in Python

"""
The complexity of the enqueue and dequeue operations of a circular queue is O(1) for (array implementations).
"""

class MyCircularQueue():

    def __init__(self, k):
        self.k = k  # k is no of elements to be enqueued
        self.queue = [None] * k  # create an empty list of size k
        self.head = self.tail = -1  # at initial, tail and head both will point to -1.

    
    # Insert into the Circular Queue
    def enqueue(self, data):
        
        # check if (REAR + 1 == FRONT), if it's True means queue is full, empty otherwise.
        if ((self.tail + 1) % self.k == self.head):
            print("Circular Queue is full")

        # check whether FRONT is pointing to -1 or not if it is then make it 0 as it will our 1st enqueue
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data # add the element at ID 0
        
        else:
            # if the REAR reaches the end , next it would be at the start of the queue
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data  # add the element at the ID where the REAR is pointing now.
            

    # Delete an element from the Circular Queue
    def dequeue(self):

        # if head is pointing to -1 means it is empty
        if self.head == -1:
            print("C-Queue is Empty!!!")

        # if head and tail is pointing then reset the value of HEAD and TAIL to -1 and return the value pointing by HEAD
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp

        else:
            # if above both conditions are false then return the element pointing by HEAD and increase the value of
            # HEAD by +1 such that it becomes zero if it was pointing to last elemnt.
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp


    # to peek the C-Queue
    def printCQueue(self):
        # whether C-Queue is empty or not
        if self.head == -1:
            print("No element in the C-Queue")
        
        # Dosplay the elements if tail > head.
        elif self.tail > self.head:
            print("Elements in Circular Queue are:", end=" ")
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


        else:
            # if tail comes before head, after performing dequeueing and enqueueing (as it is C-Queue)
            print("Elements in Circular Queue are:", end=" ")

            # print all the elements from ID head to k (size -1)
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")

            # print all the elements from ID zero to tail 
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

        # always check weheter total no. of elements == k or not. If yes then print C-Queue is full
        if ((self.tail + 1) % self.k == self.head):
            print("Queue is Full")

# Driver Code Starts
if __name__ == "__main__":
    obj = MyCircularQueue(5)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    print("Initial queue")
    obj.printCQueue()

    print("After removing an element from the queue")
    obj.dequeue()
    
    obj.printCQueue()

    obj.dequeue()
    print("Afetr 2nd element removal:")
    obj.printCQueue()
    
    obj.enqueue(6)
    # obj.enqueue(7)
    obj.printCQueue()
    
