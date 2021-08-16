"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
from typing import List


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getHash(s: str) -> int:
            hash = 0
            for ch in s:
                id = ord(ch) - ord('a') + 1
                hash += (id * (id+17) * (id+23) * (id+29) * (id+41))

            return hash

        lret = []
        existAnagram = {}
        for s in strs:
            hash = getHash(s)
            if hash in existAnagram:
                existAnagram[hash].append(s)
            else:
                ltmp = []
                ltmp.append(s)
                lret.append(ltmp)
                existAnagram[hash] = ltmp

        return lret

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        existAnagram = {}
        for s in strs:
            hash = ''.join(sorted(s))
            if hash in existAnagram:
                existAnagram[hash].append(s)
            else:
                existAnagram[hash] = [s]

        return [existAnagram[i] for i in existAnagram]
