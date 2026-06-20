class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = [0] * 26
        for i in s:
            char[ord(i)-97] +=1

        for i in t:
            char[ord(i)-97] -=1

        for count in char:
            if count !=0:
                return False
        return True