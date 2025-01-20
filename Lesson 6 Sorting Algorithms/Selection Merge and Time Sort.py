# Selection Sort Function
def selection_sort(array):
    """
    Sorts an array using the Selection Sort algorithm.
    The algorithm divides the array into a sorted and an unsorted portion.
    It repeatedly selects the smallest element from the unsorted portion
    and places it at the end of the sorted portion.

    Args:
        array (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    n = len(array)  # Get the length of the array

    for i in range(n):  # Loop through the array
        # Find the index of the smallest element in the unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the smallest element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]

    return array  # Return the sorted array
  
# Merge Function for Timsort
def merge_Time(left, right):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left (list): First sorted array.
        right (list): Second sorted array.

    Returns:
        list: Merged sorted array.
    """
    sorted_list = []
    i = j = 0

    # Compare elements and merge them into a sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Timsort Function
def timsort(array):
    """
    Sorts an array using the Timsort algorithm.
    A hybrid sorting algorithm derived from merge sort and insertion sort.

    Args:
        array (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    min_run = 32
    n = len(array)

    # Step 1: Sort small portions using Insertion Sort
    for i in range(0, n, min_run):
        insertion_sort_time(array, i, min((i + min_run - 1), n - 1))

    # Step 2: Merge sorted portions
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), n - 1)

            # Merge the two subarrays
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1]
            )

            # Place the merged array back into the original array
            array[start:start + len(merged_array)] = merged_array

        size *= 2

    return array
def insertion_sort_time(array, start=0, end=None):
    """
    Sorts a portion of the array using the Insertion Sort algorithm.

    Args:
        array (list): List of elements to be sorted.
        start (int): Starting index of the portion to sort.
        end (int): Ending index of the portion to sort (inclusive).

    Returns:
        None: The input array is modified in-place.
    """
    if end is None:
        end = len(array) - 1

    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1

        # Compare and shift elements in the sorted portion
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


# Merge Function for Merge Sort
def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.

    Args:
        left (list): First sorted array.
        right (list): Second sorted array.

    Returns:
        list: Merged sorted array.
    """
    sorted_list = []
    i = j = 0

    # Compare elements and merge them into a sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Merge Sort Function
def merge_sort(array):
    """
    Sorts an array using the Merge Sort algorithm.
    A divide-and-conquer algorithm that splits the array into halves,
    recursively sorts each half, and then merges the sorted halves.

    Args:
        array (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    if len(array) <= 1:  # Base case: arrays with 0 or 1 element are already sorted
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])  # Recursively sort the left half
    right_half = merge_sort(array[mid:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left_half, right_half)

sample=[1,3,2,24,4,3,2,1,2,1]
print(timsort(sample))
print(selection_sort(sample))
print(merge_sort(sample))

