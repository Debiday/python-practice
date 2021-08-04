#_________________________________________________________
# Check anagram
#_________________________________________________________
def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("anagrams", "nagaram"))

#_________________________________________________________
#array-pair-sum/twosum
#_________________________________________________________
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]

#_________________________________________________________
#missing number based on largest num in array
#_________________________________________________________
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortedNum = sorted(nums)
        if sortedNum[-1] == len(nums) and 0 not in nums:
            return 0;
        for i in range(len(nums)-1):
            if sortedNum[i] + 1 == sortedNum[i+1]:
                continue;
            return sortedNum[i] + 1
        return sortedNum[-1] + 1

#_________________________________________________________
# find missing element by comparing two lists
#_________________________________________________________
def finder(arr1, arr2):

    arr1.sort()
    arr2.sort()
    
    #returns a tuple, with tuple unpacking in line 42
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]

#XOR: Exclusive or for constant time
def finder2(arr1, arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num
        print result
    
    return result
#_________________________________________________________
# maximum subarray
#_________________________________________________________
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum+num, num)
            max_sum = max(current_sum, max_sum)

        return max_sum

#_________________________________________________________
#
#_________________________________________________________

#_________________________________________________________
#
#_________________________________________________________

#_________________________________________________________
#
#_________________________________________________________

#_________________________________________________________
#
#_________________________________________________________

#_________________________________________________________
#
#_________________________________________________________

#_________________________________________________________
#
#_________________________________________________________