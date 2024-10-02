class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remains = [g-c for g, c in zip(gas, cost)]

        if sum(remains) < 0:
            return -1
        
        curr_sum = 0
        idx = 0
        cnt = 0
        n = len(gas)
        while True:
            curr_sum += remains[idx]
            if curr_sum < 0:
                curr_sum = 0
                cnt = 0
            else:
                cnt += 1
                if cnt == n+1:
                    break
            # reinitialize idx
            idx = (idx+1)%n
        
        return idx


