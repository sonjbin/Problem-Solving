class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = len(citations)
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i+1:
                return i

        return h_index