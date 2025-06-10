class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = []
        stack = []
        record = []
        for p in s:
            record += p
            if p == "(":
                stack += p
            else:
                stack.pop()
            if not stack:
                output.append("".join(record[1:-1]))
                record = []

        return "".join(output)