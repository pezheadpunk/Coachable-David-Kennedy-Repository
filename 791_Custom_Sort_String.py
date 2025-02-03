'''791. Custom Sort String'''

class Solution:
    '''
    Creates a dictionary of the order string with each character as a key 
    and its index in the string as the value while also adding blank 
    strings to the indexes of the the result list where those characters
    might be placed. Then iterates over the s string's characters and if 
    they are in the order dictionary, adds that character to the string in
    the index that matched the dictionary's value. Then joins the result 
    list to one string and returns it.
    Runtime: O(n) -> iterating over the s string
    Space: O(n) -> result list
    '''
    def customSortString(self, order: str, s: str) -> str:
        result = []
        order_dict = {}
        for index, char in enumerate(order):
            order_dict[char] = index
            result.append("")
        for char in s:
            if char in order_dict:
                result[order_dict[char]] += char
            else:
                result.append(char)
        return "".join(result)