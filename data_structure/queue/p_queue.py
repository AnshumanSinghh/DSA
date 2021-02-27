# Priority Queue implementation in Python

# Function to Heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # for l < n, if left element is greater than right.Then the largest will be l
    if l < n and arr[i] < arr[l]:
        largest = l

    # for r < n, if right element is greater than the left one.Then the largest will be r
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to Insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)

    else:
        array.append(newNum)

        # After the insertion of element heapify the tree
        """
        size // 2 = Index of last non-leaf node .

        Perform reverse level order traversal from last non-leaf node and heapify each node
        """
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size - 1):
        if num == array[i]:
            break

    # Swap the nodeToBeDeleted and last element
    array[i], array[size - 1] = array[size - 1], array[i]

    eleToBeDelted = array[size - 1]

    array.remove(eleToBeDelted)  # deleting the nodeToBeDeleted
    # del array[size - 1]  # it can also be used to delete the element
    print(eleToBeDelted, "is deleted")

    # After the deletion of element heapify the tree
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)
    
# Driver Code Starts
if __name__ == "__main__":
    arr = []

    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)

    print("Max-Heap array:", arr)
    deleteNode(arr, 3)
    print("Max-Heap array:", arr)

    insert(arr, 1)
    insert(arr, 7)

    print("Max-Heap array:", arr)

    deleteNode(arr, 4)

    print("At end:", arr)
