# count reversed concatted tiny numbers < k
def countTinyPairs(a, b, k):
    
    # goal:
    # note: a and b same length
        # zip a and b(reverse)
        # if a.concat(b) < k
            # tiny
                # return num of tiny pairs
    
    rev_b = b[::-1]
       
    result = tuple(zip(a, rev_b))
    
    final = []
    
    tiny = 0
    
    for res in result:
        final.append(''.join(str(i) for i in res))
    
    for num in final:
        if int(num) < k:
            tiny += 1
    return tiny


#is Zigzag
def isZigzag(numbers):
    # goal: construct array numbers.length - 2
    # pattern: bigger than, smaller than 
        # if bigger than than: 0 and next is smaller than, follwed by bigger then: 
        # or if smaller than than: 0 and next is bigger than, follwed by smaller than: final.append(1)
            
        final = []
        
        for i in range(len(numbers)-2):
            if (numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]) or (numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]):
                final.append(1)
            else:
                final.append(0)
        return final
                
