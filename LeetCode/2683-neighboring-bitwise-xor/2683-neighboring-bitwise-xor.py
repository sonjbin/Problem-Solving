class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first_val = 0
        num = 0
        for n in derived:
            if n:
                num ^= 1
        return num == first_val