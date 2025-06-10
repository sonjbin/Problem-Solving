class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dict = {")":"(", "}":"{", "]":"["}
        for p in s:
            if p in par_dict.values():
                stack.append(p)
            elif stack and stack[-1] == par_dict[p]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
