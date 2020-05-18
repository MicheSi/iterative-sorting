def linear_search(arr, target):
    # Your code here
    # traverse through length of array
    for i in range(len(arr)):
        # if index of array is target, return index
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    #  find size of array
    left = 0
    right = len(arr) - 1

    while left <= right:
        # find midpoint of array
        mid = (left + right) // 2
        # check if midpoint is our target, if it is, return that item
        if arr[mid] == target:
            return mid
        # check if item should be left or right of midpoint
        if arr[mid] < target:
            # if less than midpoint, toss out left side and update the left index
            left = mid + 1
        # if greater than - toss out right and update right
        else:
            right = mid - 1 

    return -1  # not found
