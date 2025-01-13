class MinHeap:
    def __init__(self):
        """
        Initialize a MinHeap with an internal list to store heap elements.
        The first element (index 0) is set to 0 to simplify integer division 
        calculations for parent-child relationships.
        """
        self.heap_list = [0]  # Index 0 is not used to simplify parent-child calculations
        self.current_size = 0

    def sift_up(self, i):
        """
        Moves an element at index `i` up the heap to maintain the min-heap property.
        Stops when the element is in the correct position or reaches the root.
        """
        while i // 2 > 0:  # While there is a parent node
            # Compare current node with its parent
            if self.heap_list[i] < self.heap_list[i // 2]:
                # Swap if current node is smaller than the parent
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2  # Move up to the parent index

    def insert(self, k):
        """
        Inserts a new element `k` into the heap and maintains the min-heap property.
        """
        self.heap_list.append(k)  # Add the new element to the end
        self.current_size += 1  # Increase the size
        self.sift_up(self.current_size)  # Sift up the new element

    def sift_down(self, i):
        """
        Moves an element at index `i` down the heap to maintain the min-heap property.
        """
        while (i * 2) <= self.current_size:  # While there is at least one child
            mc = self.min_child(i)  # Get the index of the smaller child
            if self.heap_list[i] > self.heap_list[mc]:
                # Swap if the current node is greater than the smaller child
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc  # Move down to the child's index

    def min_child(self, i):
        """
        Returns the index of the smaller child of the node at index `i`.
        If there is only one child, return its index.
        """
        if (i * 2) + 1 > self.current_size:  # If there is no right child
            return i * 2  # Return left child
        else:
            # Return the index of the smaller child
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        """
        Removes and returns the smallest element (root) from the heap.
        Returns 'Empty heap' if the heap is empty.
        """
        if self.current_size == 0:  # If the heap is empty
            return 'Empty heap'
        
        root = self.heap_list[1]  # Get the root element
        # Replace the root with the last element
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()  # Remove the last element
        self.current_size -= 1  # Decrease the size
        self.sift_down(1)  # Sift down the new root to maintain the heap property
        return root

    def get_min(self):
        """
        Returns the smallest element (root) without removing it.
        """
        if self.current_size == 0:
            return 'Empty heap'
        return self.heap_list[1]

    def is_empty(self):
        """
        Checks if the heap is empty.
        Returns True if empty, False otherwise.
        """
        return self.current_size == 0

    def size(self):
        """
        Returns the number of elements in the heap.
        """
        return self.current_size


# Example usage
heap = MinHeap()
heap.insert(5)
heap.insert(9)
heap.insert(41)
heap.insert(11)
heap.insert(14)
heap.insert(18)

print("Heap list:", heap.heap_list)  # Output should reflect the min-heap structure

print("Minimum element:", heap.get_min())
print("Heap size:", heap.size())
print("Is heap empty?", heap.is_empty())
print("Deleted minimum:", heap.delete_min())
print("Heap after deleting minimum:", heap.heap_list)
