"""
Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""


class WordDictionary:

    def __init__(self):
        self.dictory = {}

    def addWord(self, word: str) -> None:
        n = len(word)
        if n not in self.dictory:
            self.dictory[n] = []

        self.dictory[n].append(word)

    def search(self, word: str) -> bool:
        def issamword(word1: str, word2: str) -> bool:
            for i in range(len(word1)):
                if word2[i] != '.' and word1[i] != word2[i]:
                    return False
            return True

        n = len(word)
        if n not in self.dictory:
            return False

        for dword in self.dictory[n]:
            if issamword(dword, word):
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)