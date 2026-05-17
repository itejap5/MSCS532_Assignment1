# MSCS532 Assignment 1
# This program demonstrates insertion sort in decreasing order.

def insertion_sort_descending(arr):
    """
    This function sorts a list in decreasing order using insertion sort.
    Example: [5, 2, 9, 1] becomes [9, 5, 2, 1]
    """

    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # Move smaller values one position to the right
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = key

    return arr


# Test the function
numbers = [31, 41, 59, 26, 41, 58]

print("Original array:")
print(numbers)

sorted_numbers = insertion_sort_descending(numbers)

print("Sorted array in decreasing order:")
print(sorted_numbers)
