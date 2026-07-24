class Solution:
    def myAtoi(self, s: str) -> int:
        

        s = s.lstrip()  # Step 1: Remove leading whitespaces
        if not s:
            return 0

        sign = 1
        index = 0
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 2: Handle sign
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3 & 4: Convert digits to integer
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            # Step 5: Handle overflow and underflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1

        return sign * result