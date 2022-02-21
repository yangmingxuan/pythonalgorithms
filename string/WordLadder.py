"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        originWords = {}
        deformWords = {}
        done = {}

        #add the wordList to Map
        for word in wordList:
            #get all the one letter deform
            for i in range(len(word)):
                deformWord = word[:i] + "#" + word[i+1:]
                oTod = originWords.setdefault(word, [])
                oTod.append(deformWord)
                originWords[word] = oTod
                dToo = deformWords.setdefault(deformWord, [])
                dToo.append(word)
                deformWords[deformWord] = dToo

        #if endWord not in the wordList
        if endWord not in originWords:
            return 0

        #add the beginWord to Map
        for i in range(len(beginWord)):
            deformWord = beginWord[:i] + "#" + beginWord[i + 1:]
            oTod = originWords.setdefault(beginWord, [])
            oTod.append(deformWord)
            #originWords[beginWord] = oTod
            dToo = deformWords.setdefault(deformWord, [])
            dToo.append(beginWord)
            #deformWords[deformWord] = dToo

        #initial
        words = []  #queue
        words.append((beginWord, 1))
        done[beginWord] = ""

        while words:
            node = words.pop(0)
            originWord = node[0]
            step = node[1]
            oTod = originWords[originWord]
            for deformWord in oTod:
                dToo = deformWords[deformWord]
                for newWord in dToo:
                    if endWord == newWord:
                        return step+1
                    if newWord not in done:
                        done[newWord] = originWord
                        words.append((newWord, step+1))

        return 0
