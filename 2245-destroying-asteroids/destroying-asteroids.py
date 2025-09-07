class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        ans = True
        for a in asteroids:
            if mass>=a:
                mass+=a
            else:
                ans = False
                break
        return ans



        