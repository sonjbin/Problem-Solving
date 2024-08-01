class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combination(a, b):
            out = []
            for c_a in a:
                for c_b in b:
                    out.append(c_a+c_b)
            return out
            
        if len(digits) == 0:
            return []

        letter_dict = dict()
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        out = [""]
        for digit in digits:
            out = combination(out, keyboard[digit])
        
        return out
        