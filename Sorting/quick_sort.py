def partition(arr, low, high): 
    '''
    This function returns partition index of an array.
    ''' 
    pivot = arr[high]  # let the last elemnt be pivot

    i = low - 1  # initializing index of smaller element

    for j in range(low, high):  # we will loop from low to high - 1

        if arr[j] < pivot:  # if low elment is lesser than then increment the i and swap them

            i += 1

            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # when arrangements have done, we have to do one more thing
                                                   # i.e, swap the high element with the element at i + 1 index
                                                   # because only by doing this pivot will satisfy all the conditions
                                                   # element before pivot must be smaller and after pivot it msust be greater
    return (i + 1)  # finally return the partition index


def quick_sort(arr, low, high): 
    """
    This function recursively calls the itsef and partition func untill all the elements get sorted.
    """
     
    if low < high:  # recursively call the funcn until low index is less than high index

        pi = partition(arr, low, high)  # store the partition index in variable pi
        
        quick_sort(arr, low, pi - 1)  # divide the array from low to (pi - 1)index as pivot element is already at it's place
        quick_sort(arr, pi + 1, high)  # and another part from (pi + 1) index to high, as pivot is alredy sorted

    return arr  # return the array after sorting is comlete

# Driver Code Starts
if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements: ").split()))
    print(quick_sort(arr, 0, len(arr) - 1))


"""
Analysis of QuickSort
Time taken by QuickSort in general can be written as following.

T(n) = T(k) + T(n-k-1) + theta(n)
The first two terms are for two recursive calls, the last term is for the partition process. k is the 
number of elements which are smaller than pivot.The time taken by QuickSort depends upon the input array 
and partition strategy. Following are three cases.

Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot. 
If we consider above partition strategy where last element is always picked as pivot, the worst case would occur 
when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.

T(n) = T(0) + T(n-1) + theta(n)
which is equivalent to  
T(n) = T(n-1) + theta(n)
The solution of above recurrence is theta(n2).

Best Case: The best case occurs when the partition process always picks the middle element as pivot. Following 
is recurrence for best case.

 T(n) = 2T(n/2) + theta(n)
The solution of above recurrence is theta(nLogn). It can be solved using case 2 of Master Theorem.

Average Case:
To do average case analysis, we need to consider all possible permutation of array and calculate time taken by 
every permutation which doesn’t look easy. We can get an idea of average case by considering the case when 
partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.

T(n) = T(n/9) + T(9n/10) + theta(n)
Solution of above recurrence is also O(nLogn)

Although the worst case time complexity of QuickSort is O(n2) which is more than many other sorting algorithms 
like Merge Sort and Heap Sort, QuickSort is faster in practice, because its inner loop can be efficiently 
implemented on most architectures, and in most real-world data. QuickSort can be implemented in different ways 
by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge 
sort is generally considered better when data is huge and stored in external storage.
"""
