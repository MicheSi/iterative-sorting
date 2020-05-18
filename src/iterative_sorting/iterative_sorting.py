# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for smallest_index in range(i + 1, len(arr)):
            if arr[smallest_index] < arr[cur_index]:
                cur_index = smallest_index
        # TO-DO: swap
        # Your code here
        arr[i], arr[cur_index] = arr[cur_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    length = len(arr)
    # loop through all array elements
    for i in range(length - 1):
        #  loop through array from 0 to length -1
        for j in range(0, length - 1 - i):
            # swap elements if greater than next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    # find max element in array
    length = len(arr)
    temp = [0] * length
    # initialize length + 1 with all elements 0 - used for storing count
    count = [0] * temp
    # store count of each element in count array
    for i in range(0, length):
        count[arr[i]] += 1
    # store cumulative sum of elements in count array
    for i in range(1, maximum):
        count[i] += count[i - 1]
    # find index of each element of original array in count array
    # decrease by 1
    i = length - 1
    while i >= 0:
        temp[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    # copy sorted elements into original array
    for i in range(0, length):
        arr[i] = temp[i]
    return arr
