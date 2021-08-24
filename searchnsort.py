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
# 
# _________________________________________________________
# _________________________________________________________
# 
# _________________________________________________________
# _________________________________________________________
# 
# _________________________________________________________
# _________________________________________________________
# 
# _________________________________________________________
# _________________________________________________________
# 
# _________________________________________________________
# _________________________________________________________
# 
# _________________________________________________________