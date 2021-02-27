def bubble_sort(arr, n): 
    '''
    In first pass the largest element will be at the last posiotion, in second pass the second largest 
    element will be at second last postion and so on.
    ''' 
    for i in range(n):
        swapped = False  # to optimize the code if code is already sorted then swapping will not performed
                         # and hence we will use this to come out of the loop

        for j in range(0, n - i - 1):  # we will traverse from the 0th index to (n - i - 1) index as in every pass
                                       # the last element will be at it's position

            if arr[j] > arr[j + 1]:  # if first element is greater than second one then swap and mark it as swapped
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:  # if swapping is not performed then break the loop
            break

    return arr  # finally return the array


# Driver Code Starts
if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements: ").split()))
    print(bubble_sort(arr, len(arr)))


"""
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

Auxiliary Space: O(1)

Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

Sorting In Place: Yes

Stable: Yes

Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
In computer graphics it is popular for its capability to detect a very small error (like swap of 
just two elements) in almost-sorted arrays and fix it with just linear complexity (2n)
"""
