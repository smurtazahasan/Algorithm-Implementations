# Simple way of expressing the unpredictability of run times
# Brute force implementation with 2 for loops
# Worst Case Time complexity: O(n^2)

def sortBubble_brute(arr, timeArr): # Alters exisiting array
    import time # Imported time to calculate runtime (s) for bubble sort algorithm only
    start = time.time() # Time since epoch
    for i in range(len(arr)):
        # Iterates the list; acts as an overall counter
        for j in range(len(arr)-1):
            # Iterates the entire list for every iteration of var i
            if arr[j] > arr[j+1]: # If mismatch is found; swaps the items
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    stop = time.time() # stops the meansuring of time
    timeArr.append(stop-start)

def randArr(n): # acts as a random list generator for n elements
    import random
    newArr = []
    # Efficient alternative could have been utilizing NumPy library
    for i in range(n - 1):
        newArr.append(random.randint(0, 999)) # Change range of numbers if needed
    return newArr

def multipleIterations(iterations, elements): # To asses for multiple iterations
    algoTime = [] # Stores the run time for each iteration
    for i in range(iterations):
        sortBubble_brute(randArr(elements), algoTime) # Sorts the random array and saves runtimes
    return algoTime # Returns the only important list

def printResults(algoTime, iterations): # Inefficient way of displaying run times
    avgTime = 0
    for i in range(len(algoTime) - 1):
        print('Iteration ', i+1, ': ', algoTime[i])
        avgTime = avgTime + algoTime[i]
    avgTime = avgTime/iterations # Acquires the Avg. runtime
    print('Average Time for ', iterations, ' iterations: ', avgTime, 's')


printResults(multipleIterations(1000, 100), 1000)
# Takes in: No. of iterations, No. of elements inside of arrays, No. of iterations for averaging
# ('Average Time for ', 1000, ' iterations: ', 0.0009233038425445557, 's')
