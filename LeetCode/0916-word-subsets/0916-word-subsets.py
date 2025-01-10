class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b_cnt_list = []
        alphas = 'abcdefghijklmnopqrstuvwxyz'
        for i,c in enumerate(alphas):
            max_cnt = 0
            for w in words2:
                cnt = w.count(c)
                if cnt > max_cnt:
                    max_cnt = cnt
            b_cnt_list.append(max_cnt)

        result = []
        for a in words1:
            is_subset = True
            for i, c in enumerate(alphas):
                if a.count(c) < b_cnt_list[i]:
                    is_subset = False
                    break
            if is_subset:
                result.append(a)

        return result 
