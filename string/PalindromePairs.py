"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""
from typing import List


class PalindromePairs:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalidromeString(word: str, l: int, r: int) -> bool:
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def prefixPalidrome(word: str) -> List[str]:
            prefix = []
            for i in range(len(word)):
                if isPalidromeString(word, i, len(word)-1):
                    prefix.append(word[:i])
            return  prefix

        def suffixPalidrome(word: str) -> List[str]:
            suffix = []
            for i in range(len(word)):
                if isPalidromeString(word, 0, i):
                    suffix.append(word[i+1:])
            return suffix

        ans: List[List[int]] = []
        wordIndex = {word[::-1] : i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            #find the reverse word
            #reverseWord = word[::-1]
            if word in wordIndex and wordIndex[word] != i:
                ans.append([i, wordIndex[word]])

            #find the prefix's reverse word, word+reversePrefix will be palidrome
            for prefix in prefixPalidrome(word):
                #reversePrefix = prefix[::-1]
                if prefix in wordIndex:
                    ans.append([i, wordIndex[prefix]])

            #find the suffix's reverse word, reverseSuffix+word will be palidrome
            for suffix in suffixPalidrome(word):
                #reverseSuffix = suffix[::-1]
                if suffix in wordIndex:
                    ans.append([wordIndex[suffix],i])

        return ans


    def palindromePairs2(self, words: List[str]) -> List[List[int]]:
        dic = {word[::-1] : i for i, word in enumerate(words)}
          
        ans = []
        for i, word in enumerate(words):
            
            for j in range(len(word)):
                left = word[:j]
                right = word[j:]
                
                if left in dic and right == right[::-1] and dic[left] != i:
                    ans.append([i, dic[left]])
                    if left == "":
                        ans.append([dic[left], i])
                if right in dic and left == left[::-1] and dic[right] != i:
                    ans.append([dic[right], i])
                                        
        return ans

