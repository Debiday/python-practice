# _________________________________________________________
# Recursion basics recap
# _________________________________________________________
def fact(n):

    # base case
    if n == 0:
        return 1

    else:
        return n * fact(n-1)
# _________________________________________________________
# Example problems: Sum to N (e.g. 4 3 2 1 0)
# _________________________________________________________
def rec_sum(n):

    # base case
    if n == 0:
        return 0

    else:
        return n + rec_sum(n-1)
# _________________________________________________________
# Example problems: Add individual digits of an int
# _________________________________________________________
def sum_func(n):

    str_num = str(n)
    #TODO: Remember this is how to split into chars
    split = list(str_num)
    total = 0

    # base case
    if n == 0:
        return 0

    for num in split:
        total += int(num)

    return total

# or recursively!
def sum_func2(n):

    if len(str(n)) == 1: 
        return n

    else:
        return n%10 + sum_func2(n//10)    
# _________________________________________________________
# Determine if its possible to split the string to make individual words in list
# _________________________________________________________
def word_split(phrase, list_of_words, output = None):

    if output is None:
        output = []

    for word in list_of_words:
        
        if phrase.startswith(word):

            output.append(word)

            #recursively call the split function on the remaining of the phrase
            return word_split(phrase[len(word):], list_of_words, output)
    
    return output
# _________________________________________________________
# Reverse a string
# _________________________________________________________
def reverse(s):

    final = []

    if len(s) == 1:
        return s

    else:
        for char in s:
            final.insert(0, char)
        #todo: turn list into string
        return "".join(final)

#recursively...
def reverse2(s):

    # base case: how to know you are done, not edge case
    # e.g. 'abc' ------> 'c' + rev('ab') 
    # one element left in string

    if len(s) <= 1:
        return s

    # recursion

    return reverse(s[1:]) + s[0]
# _________________________________________________________
# Return all permutations of s
# _________________________________________________________
# def permute(s):
#     output = []
    
#     if len(s) <= 1:
#         output=[s]
#     else:
#         for i, let in enumerate(s):
#             for perm in permute(s[:i]+s[i+1:]):
#                 output+=[let+perm]
#     return output

# recursively...
def permute(s):
    output = []
    
    if len(s) <= 1:
        output=[s]
    else:
        for i, let in enumerate(s):
            for perm in permute(s[:i]+s[i+1:]):
                output+=[let+perm]
                print("perm is:", perm, "i is:", i, "out is:", output)
    return output
# _________________________________________________________
# Fibonnaci multiple ways, return nth fib number
# _________________________________________________________
# todo: Recursively
def fib_rec(n):

    # base case
    if n <= 1:
        return n

    # recursive case
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# todo: Dynamically
# instantiate cache information (memoization)

# cache
n = 10 # need to edit
cache = [None] * (n + 1)

def fib_dyn(n):

    # base case
    if n == 0 or n == 1:
        return n

    #check cache
    if cache[n] != None:

        return cache[n]

    # keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]

# todo: Iteratively
# todo: consider tuple unpacking
def fib_iter(n):

    a, b = 0, 1

    for i in range(n):

        a, b = b, a + b # a very pythonic solution
        # print(a)
    
    return a
# _________________________________________________________
# Coin change problem (classic and memo)
# _________________________________________________________
# Goal: fewest num of coins used
def rec_coin(target, coins):
    
    # default value set to target
    min_coins = target

    # base case
    if target in coins:
        return 1

    else:

        # for every coin value that is <= target
        # list comprehension
        for i in [c for c in coins if c <= target]:
            
            # add a coin count + recursive call
            num_coins = 1 + rec_coin(target-i, coins)

            if num_coins < min_coins:

                min_coins = num_coins

    return min_coins    
    # inefficient but it'll work!

# todo: dynamic, much faster but more space
def rec_coin_dynam(target, coins, known_results):

    # default output to target
    min_coins = target

    #base case
    if target in coins: 
        known_results[target] = 1
        return 1

    # return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    else:

        # for every coin value is <= target

        for i in [c for c in coins if c <= target]:

            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)

            if num_coins < min_coins:

                min_coins = num_coins

                # reset known results
                known_results[target] = min_coins

    return min_coins