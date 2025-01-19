class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []
        output = 0
        symbols = ["I", "V", "X", "L", "C", "D", "M"]
        values = [1, 5, 10, 50, 100, 500, 1000]
        val_dict = {c:v for c,v in zip(symbols, values)}

        for c in s:
            if stack and val_dict[stack[0]] < val_dict[c]:
                output += val_dict[c] - val_dict[stack[0]] * len(stack)
                stack = []
            else:
                for c_ in stack:
                    output += val_dict[c_]
                stack = [c]
        
        for c in stack:
            output += val_dict[c]
        
        return output

