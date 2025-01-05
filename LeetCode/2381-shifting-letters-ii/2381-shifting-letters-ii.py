class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_cnt = [0] * (n+1)
        # Generate difference array
        for start, end, d in shifts:
            add = 1 if d else -1
            shift_cnt[start] += add
            shift_cnt[end+1] -= add
        # calculate accumulate sum
        for i in range(1,n):
            shift_cnt[i] += shift_cnt[i-1]
        result = []
        for i, c in enumerate(s):
            diff = (ord(c) + shift_cnt[i] - ord('a')) % 26

            result.append(chr(diff + ord('a')))

        return ''.join(result)