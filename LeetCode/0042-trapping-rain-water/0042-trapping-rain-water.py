class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        s = 0
        output = 0
        max_idx = height.index(max(height))
        pond = 0
        for h in height[:max_idx+1]:
            if h >= s:
                s = h
                output += pond
                pond = 0
            else: 
                pond += s - h 
        s = 0
        pond = 0
        for h in height[max_idx:][::-1]:
            if h >= s:
                s = h
                output += pond
                pond = 0
            else: 
                pond += s - h 

        return output