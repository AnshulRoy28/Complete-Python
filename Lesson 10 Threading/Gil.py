# GIL (Global Interpreter Lock) is a lock that allows only one thread to execute Python bytecode at a time.
# This is important because Python uses reference counting for memory management.
# Reference counting keeps track of the number of references to an object.
# When this count reaches zero, the memory occupied by the object is released.

import sys
import time
from threading import Thread
from multiprocessing import Process

a = []  # Create an empty list
b = a   # Reference 'a' with 'b'
print(sys.getrefcount(a))  # Get the reference count of 'a'

# Here, the reference count of the empty list is 3:
# 1. The list itself
# 2. 'b' referencing 'a'
# 3. The function call to 'getrefcount'

# The GIL is needed because modifying the reference count in a multithreaded environment can lead to race conditions.
# If two threads modify the reference count simultaneously, it may result in memory leaks or crashes.
# The GIL ensures safe memory management by preventing simultaneous modifications of shared data.

COUNT = 50_000_000

def countdown(n):
    while n > 0:
        n -= 1

# Single-threaded execution
start = time.time()
countdown(COUNT)
end = time.time()
print('Time taken in seconds (single-threaded):', end - start)

# Multithreaded execution
# Despite using two threads, Python's GIL will not allow true parallel execution.
# This means the execution time won't be significantly improved.

t1 = Thread(target=countdown, args=(COUNT // 2,))
t2 = Thread(target=countdown, args=(COUNT // 2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds (multithreaded):', end - start)

# The expected result is that the multithreaded version takes nearly the same time as the single-threaded version.
# This is because the GIL forces Python threads to execute one at a time despite having multiple threads.
# To achieve true parallelism in CPU-bound tasks, we need multiprocessing instead of multithreading.

# Multiprocessing Execution (Bypasses GIL)
if __name__ == "__main__":
    p1 = Process(target=countdown, args=(COUNT // 2,))
    p2 = Process(target=countdown, args=(COUNT // 2,))

    start = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()

    print('Time taken in seconds (multiprocessing):', end - start)

# The multiprocessing version should be significantly faster than the multithreaded version
# since it runs on multiple CPU cores, bypassing the GIL limitation.
