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
# 
# _________________________________________________________
# _________________________________________________________
# 
# _________________________________________________________