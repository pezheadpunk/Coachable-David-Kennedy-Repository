'''1249. Minimum Remove to Make Valid Parentheses'''

class Solution:
    '''Solution Class'''
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        The string is conveted into a list and then iterates over the list, and
        if the character is a "(" it adds its index to the stack and changes
        that index to "". If the character is a ")" and the stack is not empty,
        it adds a '(' to the index in the result list. Then it returns the
        result list as a string that is joined by "".
        Runtime: O(n)
        Space: O(n)
        '''
        result = list(s)
        stack = []
        for i in range(len(s)):
            if result[i] == '(':
                stack.append(i)
                result[i] = ""
            elif result[i] == ')':
                if stack:
                    result[stack.pop()] = '('
                else:
                    result[i] = ""
        return "".join(result)
