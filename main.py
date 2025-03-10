class Solution:
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result

def int_to_roman(num):
    return Solution().intToRoman(num)
