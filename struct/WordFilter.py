"""
Prefix and Suffix Search
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.


Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".


Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
"""
from typing import List


class Trie:
    def __init__(self):
        self.links = {}
        self.IDX = []

class WordFilter:

    #For another idea, see the java algorithm
    def __init__(self, words: List[str]):
        self.root = Trie()
        self.WORDS = words

        for idx, word in enumerate(words):
            #store all word and its idx
            node = self.root
            for ch in word:
                if ch not in node.links:
                    node.links[ch] = Trie()
                node = node.links[ch]
                node.IDX.append(idx)

    def f(self, prefix: str, suffix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.links:
                return -1
            node = node.links[ch]

        wordidx = node.IDX
        for j in range(len(wordidx)-1, -1, -1):
            if(self.WORDS[wordidx[j]].endswith(suffix)):
                return wordidx[j]

        return -1

