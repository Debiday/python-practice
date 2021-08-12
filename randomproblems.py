#_____________________________________________________________
# count reversed concatted tiny numbers < k
#_____________________________________________________________
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

#_____________________________________________________________
# is Zigzag
#_____________________________________________________________
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


#_____________________________________________________________
# jumping on clouds
#_____________________________________________________________                
def jumpingOnClouds(c):
    # jump in multiples of two!

    current_position = 0
    number_of_jumps = 0
    last_cloud_postion = len(c)-1
    last_second_postion = len(c)-2
    
    while current_position<last_second_postion:
        #Checking if the cloud next to the next cloud is thunderstorm
        if c[current_position+2] == 0:
            current_position += 2
        else:
            current_position += 1
        number_of_jumps += 1
    #Checking if we are in the last cloud or the last second cloud
    if current_position != last_cloud_postion:
        number_of_jumps += 1
        
    return number_of_jumps

# dropbox

def textEditor1_2(queries):
    #apply result, then append the current state
    print(queries[1])
    
    result = ""
    final_list = []
    index = 0
    
    for action in queries:
        if action[0] == "APPEND":
            if action[1] == "START. ":
                index = 0
                result = "START. " + result
                final_list.append(result)
            elif action[1] == "END.":
                result += "END." 
                index = len(result)-1
                final_list.append(result)
            else:
                result = result[0: index] + action[1] + result[index: len(result)]
                index += len(action[1])
                final_list.append(result)
        elif action[0] == "MOVE":
            index = int(action[1])
        elif action[0] == "BACKSPACE" and index != 0:
            result = result[:index-1] + result[index:]
            index -= 1
            final_list.append(result)
        elif action[0] == "BACKSPACE" and index == 0:
            result = ""
            final_list.append(result)
        elif action[0] == "SELECT":
            if int(action[1]) == int(action[2]):
                index = int(action[1])
            result = result[:int(action[1])+2] + result[int(action[2])-1:]
            index = int(action[1])
            
            
    return final_list
    

