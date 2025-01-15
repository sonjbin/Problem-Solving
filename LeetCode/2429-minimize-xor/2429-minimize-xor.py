class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_bits = bin(num2).count('1')
        
        # Generate a list of bits set in num1
        num1_bits = list(bin(num1)[2:])
        num1_bits = ['0'] * (32 - len(num1_bits)) + num1_bits

        # Greedily try to set the highest bits in num1 first
        result_bits = ['0'] * 32
        for i in range(32):
            if num2_bits > 0 and num1_bits[i] == '1':
                result_bits[i] = '1'
                num2_bits -= 1

        # If there are still bits left to set, set them from the lowest bit
        for i in range(31, -1, -1):
            if num2_bits > 0 and result_bits[i] == '0':
                result_bits[i] = '1'
                num2_bits -= 1

        # Convert result_bits back to an integer
        result = int(''.join(result_bits), 2)
        return result