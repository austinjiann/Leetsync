class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(curr, index):
            if len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return
            possible = letters[digits[index]]
            for letter in possible:
                curr.append(letter)
                backtrack(curr,index+1)
                curr.pop()
                
        backtrack([], 0)
        return ans