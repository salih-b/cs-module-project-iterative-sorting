# TO-DO: Complete the selection_sort() function below
# runtime: O(n * n) = O(n^2)
def selection_sort(arr):
    # iterate through the array (represents the sorted-unsorted cur_index 
    # moving across the array)
    for i in range(len(arr)):  # O(n)
        # index of the cur_index, as well as the index we're going to 
        # swap the smallest element with 
        # cur_index = i
        cur_index = i

        smallest_value = arr[cur_index]
        smallest_index = cur_index
        # smallest_index = cur_index
        # finding the smallest element 
        # in the "unsorted" portion of the array 
        for unsorted_index in range(cur_index, len(arr)):  # O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # `smallest_index` is the index of the smallest element in the unsorted portion 

        # once that's found, swap it with the element on the right edge 
        # of the sorted-unsorted cur_index 

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


arr = [5, 55, 6, 67, 12, 9, 25, 43, 16]
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # we know all the elements are in sorted order when we do a full
    # pass through the array and perform no swaps 
    swaps_occurred = True
    # iterating through the arr and looking at elements two at a time 
    # swapping them if they're out of order 
    while swaps_occurred:
        swaps_occurred = False
        # if we do this all the way through, all the elements will 
        # eventually end up in sorted order 
        for i in range(len(arr) - 1):
            # we need to swap if arr[i] > arr[i+1]
            if arr[i] > arr[i+1]:
                # swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
