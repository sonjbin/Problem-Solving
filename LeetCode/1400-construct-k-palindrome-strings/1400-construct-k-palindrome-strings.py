class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        counter = Counter(s)
        cnt_pairs = 0
        cnt_single = 0
        for n in counter.values():
            cnt_pairs += n//2
            cnt_single += n%2
        print(cnt_single, cnt_pairs)
        if cnt_single > k or cnt_pairs*2 + cnt_single < k:
            return False
        return True