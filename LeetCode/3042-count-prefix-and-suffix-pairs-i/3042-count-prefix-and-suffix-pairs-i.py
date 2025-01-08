class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a, b):
            if a == b[:len(a)] == b[-1*len(a):]:
                return True
            return False
        cnt = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    cnt += 1
        
        return cnt