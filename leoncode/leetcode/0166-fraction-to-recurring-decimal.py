# 166 - https://leetcode.com/problems/fraction-to-recurring-decimal/

# Time: O(N) - N is the number of digits in the decimal representation
# Space: O(N)

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        if denominator == 0: raise Exception("division by zero error")

        res = []
        sign = ""
        if (numerator < 0) ^ (denominator < 0):
            # negative number
            sign = "-"
    
        # cleanup signs
        numerator, denominator = abs(numerator), abs(denominator)
        quotient = numerator // denominator
        remainder = numerator % denominator

        res.append(sign)
        res.append(str(quotient))

        if remainder == 0:
            return ''.join(res)
        
        # there is remainder, continue dividing
        res.append(".")

        remainder_map = {} # keeps track of seen remainders
        
        while remainder != 0:
            if remainder in remainder_map:
                repeat_loc = remainder_map[remainder]
                res.insert(repeat_loc, "(")
                res.append(")")
                return ''.join(res)

            remainder_map[remainder] = len(res)
            remainder *= 10
            decimal = remainder // denominator
            res.append(str(decimal))
            remainder = remainder % denominator
            
        return ''.join(res)