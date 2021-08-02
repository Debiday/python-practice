# Check anagram
def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("anagrams", "nagaram"))
