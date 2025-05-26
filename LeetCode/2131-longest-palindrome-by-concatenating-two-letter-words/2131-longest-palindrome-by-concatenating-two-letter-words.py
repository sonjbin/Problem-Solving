class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict, rev_dict = defaultdict(int), defaultdict(int)

        for w in words:
            word_dict[w] += 1
            rev_dict[w[::-1]] += 1
        result = 0
        for w, n in rev_dict.items():
            if w in word_dict:
                num_pairs = min(n, word_dict[w])
                if w[0] == w[1]:
                    num_pairs = (num_pairs//2) * 2
                result += 2 * num_pairs
                word_dict[w] -= num_pairs
        
        remain_palindrome_words = [k for k, v in word_dict.items() if v and k[0] == k[1]]
        if remain_palindrome_words:
            result += 2
        
        return result
