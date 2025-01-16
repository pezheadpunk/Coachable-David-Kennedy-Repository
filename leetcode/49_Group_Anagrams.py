'''49. Group Anagrams'''
from collections import defaultdict
from typing import List

class Solution:
    '''Solution Class'''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Uses a dictionary that keeps the sorted words as
        tuples as keys and then adds to the value list if a
        word when sorted matches a key. Then returns the value
        lists as a list.'''
        anagram_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagram_dict[key].append(word)
        return list(anagram_dict.values())
