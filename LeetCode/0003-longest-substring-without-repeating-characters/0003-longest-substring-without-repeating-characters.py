class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        char_list = []
        for i in range(len(s)):
            temp_len = 0
            for j in range(i, len(s)):
                if s[j] not in char_list:
                    temp_len += 1
                    char_list.append(s[j])
                else:
                    char_list = []
                    break
            longest_len = max(longest_len, temp_len)

        return longest_len