from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        repeat = defaultdict(int)
        ans = 0
        for i in range (len(arr)):
            repeat[arr[i]] += 1
        sorted_items = sorted(repeat.items(), key=lambda x: x[1], reverse=True)
        length = len(arr)
        for x, y in sorted_items:
            length-=y
            ans += 1
            if length<= len(arr)/2:
                break
        return ans

        