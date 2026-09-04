class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words = {}

        for word in s:
            if word not in words:
                words[word] = 1
                continue
            words[word] += 1
        
        for word in t:
            if word not in words:
                return False
            words[word] -= 1
        
        for key in words:
            if words[key] != 0:
                return False
        
        return True
