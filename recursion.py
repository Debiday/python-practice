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
# Example problems: Add indidual digits of an int
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
# Determine if its possible to split the string to make individual words in list
# _________________________________________________________
def word_split(phrase, list_of_words, output = None):



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










