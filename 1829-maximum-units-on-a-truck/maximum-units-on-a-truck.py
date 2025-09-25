
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        rev = []
        for i in range (len(boxTypes)):
            rev.append([boxTypes[i][1],boxTypes[i][0]])
        ans = 0
        rev.sort()
        
        for i in range (truckSize):
            if (len(rev)>0):
                ans += rev[-1][0]
                rev[-1][1] -= 1
                if (rev[-1][1]) == 0:
                    rev.pop()
        return ans

        
        
        