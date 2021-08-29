# _________________________________________________________
# sequential(most basic, efficient)
# _________________________________________________________
def ordered_seq_search(arr, ele):
    """
    Input arr must be ordered/sorted
    """
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == ele:
            found = True

        else: 

            if arr[pos] > ele:
                stopped = True

            else:
                pos += 1
        
    return found
# _________________________________________________________
# Binary Search
# _________________________________________________________
def binary_search(arr, ele):
    """
    sorted array
    """

    first = 0
    last = len(arr)-1

    found = False

    while first <= last and not found:

        mid = (first+last)/2 

        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else: 
                first = mid + 1
    return found
# _________________________________________________________
# recursive bs
# _________________________________________________________
def rec_bin_search(arr, ele):

    if len(arr) == 0:
        return False

    else:

        mid = int(len(arr)/2)

        if arr[mid] == ele:
            return True

        else: 
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)

            else:
                return rec_bin_search(arr[mid+1:], ele)        
# _________________________________________________________
# hashing
# _________________________________________________________
#python has dict 
class HashTable(object):

    def __init__(self, size):

        self.size = size
        self.slots = [None] * self.size
        # none is a list with no items, e.g list of 'None's
        self.data = [None] * self.size

    def put(self, key, data):

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else: 

            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data 

            else:

                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return(oldhash + 1)%size

    def get(self, key):

        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position =  self.rehash(position, len(self.slots))
                if position == startslot:

                    stop = True
        return data

    def __getitem__(self, key):
        # special methods for python indexing
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
# _________________________________________________________
# bubble sort
# _________________________________________________________
def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):

            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr
# _________________________________________________________
# selection sort
# _________________________________________________________
def selection_sort(arr):

    for fillslot in range(len(arr)-1, 0, -1):

        positionOfMax = 0

        for location in range(1, fillslot+1):

            if arr[location] > arr[positionOfMax]:
                positionOfMax = location

        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp
        #switch
# _________________________________________________________
# insertion sort
# _________________________________________________________
#less efficient on large lists than more advanced algos such as
#quicksort, heapsort or mergesort
def insertion_sort(arr):

    for i in range(1, len(arr)):

        currentvalue = arr[i]
        position = i 

        #sorted sublist
        while position > 0 and arr[position-1] > currentvalue:

            arr[position] = arr[position-1]
            position = position - 1

        arr[position] = currentvalue
# _________________________________________________________
# shell sort (improves the insertion sort)
# _________________________________________________________
#final pass uses an insertion sort
def shell_sort(arr):

    sublistcount =  len(arr)/2

    while sublistcount > 0:
        for start in range(int(sublistcount)):

            gap_insertion_sort(arr, start, int(sublistcount))

        # print('After increments of size: ', sublistcount)
        # print('The list is ', arr)

        sublistcount = sublistcount/2

def gap_insertion_sort(arr, start, gap):

    for i in range(start + gap, len(arr), gap):

        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position-gap] > currentvalue:

            arr[position] = arr[position-gap]
            position = position-gap

        arr[position] = currentvalue

# _________________________________________________________
# merge sort
# _________________________________________________________
#recursive algo that continually splits the list in half
def merge_sort(arr):

    #base case
    if len(arr) > 1:

        mid = int(len(arr)/2)
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        #recursive
        merge_sort(lefthalf)
        merge_sort(righthalf)

        #counters
        i = 0 
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]

                i += 1
            
            else:
                arr[k] = righthalf[j]
                j += 1
            
            k += 1
            
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

    print('Merging ', arr)
# _________________________________________________________
# quick sort
# _________________________________________________________
#pivot value
def quick_sort(arr):
    
    quick_sort_help(arr, 0, len(arr)-1)

def quick_sort_help(arr, first, last):
    
    if first < last:

        splitpoint = partition(arr, first, last)

        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)

def partition(arr, first, last):
    
    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last 

    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:

            leftmark += 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True

        else: 
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark