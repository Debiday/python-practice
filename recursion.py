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
# def permute2(s):

#     out = []
    
#     # base case
#     if len(s) == 1:
#         out = [s]

#     else: 

#         for i, let in enumerate(s):

#             #for every permutation resulting from step 2 & 3
#             for perm in permute2( s[:i] + s[i+1:]):
#                 print("perm is:", perm, "i is:", i, "out is:", out)

#                 # add it to the output
#                 out += [let + perm]

#         return out
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










