class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        jewels = list(jewels)

        for jewel in jewels:
            total += stones.count(jewel)

        return total