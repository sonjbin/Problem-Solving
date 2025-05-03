class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_list = [1e9] * 6
        n = len(tops)
        merged = [tops, bottoms]

        for target in range(1,7):
            for loc in range(2):
                rot = 0
                for i in range(n):
                    if merged[loc][i] != target:
                        if merged[(loc+1)%2][i] == target:
                            rot += 1
                        else:
                            rot = -1
                            break
                min_list[target-1] = min(min_list[target-1], rot)
        
        if max(min_list) == -1:
            return -1
        
        min_rot = min([x for x in min_list if x >= 0])

        return min_rot
