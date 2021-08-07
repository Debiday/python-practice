#_________________________________________________________
# Recursion basics recap
#_________________________________________________________
def fact(n):

    #base case
    if n == 0:
        return 1

    else:
        return n * fact(n-1)
#_________________________________________________________
# Example problems: Sum to N (e.g. 4 3 2 1 0)
#_________________________________________________________
def rec_sum(n):

    #base case
    if n == 0:
        return 0

    else: 
        return n + rec_sum(n-1)
#_________________________________________________________
# Example problems: Add indidual digits of an int
#_________________________________________________________
def sum_func(n):

    split_num = str(n).split()    

    #base case
    if n == 0:
        return 0

    else: 
        return split_num

