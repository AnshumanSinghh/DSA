# Stack implementation in Python
"""   
For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).   
"""
# Creating Stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# Adding items into the Stack
def push(stack, item):
    stack.append(item)
    print("pushed item:", item)


# Removing an elemnt from Stack, last added element will be popped
def pop(stack):
    if check_empty(stack):
        return "stack is empty!!!"
    return stack.pop()


# Driver Code Starts
if __name__ == "__main__":
    stack = create_stack()
    push(stack, str(1))
    push(stack, str(2))
    push(stack, str(3))
    push(stack, str(4))
    push(stack, str(5))
    print("popped item: " + pop(stack))
    print("stack after popping an element:", stack)
