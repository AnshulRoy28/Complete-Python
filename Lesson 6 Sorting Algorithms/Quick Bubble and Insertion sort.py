import random  # Importing the random module for generating random pivot in quicksort

# Bubble Sort Function
def bubble_sort(array):
    """
    Sorts an array using the Bubble Sort algorithm.
    Repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order.
    
    Args:
        array (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    """
    n = len(array)  # Get the length of the array
    for i in range(n):  # Outer loop for each pass through the array
        for j in range(n - i - 1):  # Inner loop for comparing adjacent elements
            if array[j] > array[j + 1]:  # If the current element is greater than the next
                array[j], array[j + 1] = array[j + 1], array[j]  # Swap the elements

    return array  # Return the sorted array

# Insertion Sort Function
def insertion_sort(array):
    """
    Sorts an array using the Insertion Sort algorithm.
    Builds the sorted list one element at a time by comparing
    and inserting elements into their correct position.
    
    Args:
        array (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    """
    for i in range(1, len(array)):  # Loop through elements starting from the second
        key = array[i]  # The current element to be inserted
        j = i - 1  # Index of the previous element

        # Shift elements of the sorted portion to the right
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key  # Insert the key element at the correct position
    return array  # Return the sorted array

# Quicksort Function
def quicksort(array):
    """
    Sorts an array using the Quicksort algorithm.
    A divide-and-conquer algorithm that partitions the list
    around a pivot element and recursively sorts the partitions.
    
    Args:
        array (list): List of elements to be sorted.
    
    Returns:
        list: Sorted list.
    """
    if len(array) < 2:  # Base case: arrays with 0 or 1 element are already sorted
        return array
    
    # Initialize partitions
    low, same, high = [], [], []

    # Choose a random pivot element
    pivot = array[random.randint(0, len(array) - 1)]

    # Partition the array into low, same, and high based on the pivot
    for item in array:
        if item < pivot:  # Elements smaller than pivot go to 'low'
            low.append(item)
        elif item == pivot:  # Elements equal to pivot go to 'same'
            same.append(item)
        elif item > pivot:  # Elements greater than pivot go to 'high'
            high.append(item)
    
    # Recursively apply quicksort to partitions and combine the results
    return quicksort(low) + same + quicksort(high)

# Sample data to test the sorting algorithms
sample = [1, 3, 2, 24, 4, 3, 2, 1, 2, 1]

# Print sorted results for each algorithm
print("Bubble Sort Result:", bubble_sort(sample.copy()))  # Use .copy() to avoid modifying the original list
print("Insertion Sort Result:", insertion_sort(sample.copy()))
print("Quicksort Result:", quicksort(sample.copy()))

write todays post based on this code
