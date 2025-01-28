'''227. Basic Calculator II'''

class Solution:
    '''Solution Class'''
    def calculate(self, s: str) -> int:
        '''
        Uses a stack to keep track of the values that need to still be added
        or subtracted. Iterates through the string and keeps track of the
        previous operator so that when another is encountered if the previous
        operator is multiplication or division, it does the operation on the
        last value in the stack with the current value. The values are
        calculated by multiplying the current value by ten and then adding the
        new digit of the value to the value. Then at the end the values in the
        stack are summed and the result is returned.
        Runtime: O(n) -> for loop over every character in s
        Space: O(n) -> the stack
        '''
        stack = []
        prev_sign = "+"
        value = 0
        for i in range(len(s)):
            if s[i].isdigit():
                value = value * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s)-1:
                if prev_sign == "+":
                    stack.append(value)
                elif prev_sign == "-":
                    stack.append(-value)
                elif prev_sign == "*":
                    stack.append(stack.pop() * value)
                elif prev_sign == "/":
                    stack.append(int(stack.pop() / value))
                value = 0
                prev_sign = s[i]
        result = 0
        for val in stack:
            result += val
        return result
