class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        longest_len = 0
        start = 0
        
        for end, c in enumerate(s):
            if c in char_index_map and char_index_map[c] >= start:
                start =  char_index_map[c] + 1
            char_index_map[c] = end
            longest_len = max(longest_len, end-start+1)

        return longest_len