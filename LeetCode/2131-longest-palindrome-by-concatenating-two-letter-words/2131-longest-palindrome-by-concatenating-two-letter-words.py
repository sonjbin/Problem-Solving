class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        result = 0
        has_middle = False

        for word in list(counter.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = counter[word] // 2
                result += pairs * 4  
                counter[word] -= pairs * 2
                if counter[word] > 0:
                    has_middle = True 
            elif word < rev:
                pair_count = min(counter[word], counter[rev])
                result += pair_count * 4
                counter[word] -= pair_count
                counter[rev] -= pair_count

        if has_middle:
            result += 2

        return result
