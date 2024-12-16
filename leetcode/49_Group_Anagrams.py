'''49. Contains Duplicate'''
class Solution:
    '''Solution Class'''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Uses a dictionary that keeps the sorted words as
        tuples as keys and then adds to the value list if a
        word when sorted matches a key. Then returns the value
        lists as a list.'''
        anagram_dict = {}
        for word in strs:
            key = list(word)
            key.sort()
            if tuple(key) not in anagram_dict:
                anagram_dict[tuple(key)] = []
            anagram_dict[tuple(key)].append(word)
        return list(anagram_dict.values())
