'''71. Simplify Path'''

class Solution:
    '''Solution Class'''
    def simplifyPath(self, path: str) -> str:
        '''
        Creates a list from the string, splitting each value by "/". Then 
        iterates over the list and creates a stack of the values and if
        the value is a specific string it is not added to the stack but
        if it's "..", it removes the last value in stack. Then returns the 
        stack as a string joined by "/" with a "/" added to the beginning
        of the string.
        '''
        path = path.split("/")
        stack = []
        for val in path:
            if val == ".." and stack:
                stack.pop()
            elif val not in {"", ".", ".."}:
                stack.append(val)
        return "/" + "/".join(stack)
