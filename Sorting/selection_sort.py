def selection_sort(arr, n):
    for i in range(n):
        min_id = i

        for j in range(i + 1, n):

            if arr[min_id] > arr[j]:
                min_id = j 

        arr[min_id], arr[i] = arr[i], arr[min_id]
    
    return arr

# Driver Code Starts
if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements: ").split()))
    print(selection_sort(arr, len(arr)))

"""
Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write 
is a costly operation.

Exercise :
Sort an array of strings using Selection Sort

Stability : The default implementation is not stable. However it can be made stable. Please see stable selection 
sort for details.

In Place : Yes, it does not require extra space.
"""
