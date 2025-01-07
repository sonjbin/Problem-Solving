class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        word_sum = " ".join(words)
        sub_list = [w for w in words if word_sum.count(w) > 1]

        return sub_list