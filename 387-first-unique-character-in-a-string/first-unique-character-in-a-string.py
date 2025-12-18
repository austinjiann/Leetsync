
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        seen = defaultdict(int)
        ans = []
        for i in range (len(s)):
            seen[s[i]] += 1
        for key in seen.keys():
            if seen[key] == 1:
                return s.index(key)
        return -1
            
        
            
                