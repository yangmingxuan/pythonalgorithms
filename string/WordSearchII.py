"""
 * Given a 2D board and a list of words from the dictionary, find all words in the board.

    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



    Example:

    Input:
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]

    Output: ["eat","oath"]


    Note:

    All inputs are consist of lowercase letters a-z.
    The values of words are distinct.

"""
import itertools
from typing import List


class TrieNode:
    links = None
    word: str = None

    def __init__(self):
        #self.links = [None] * 26
        self.links = {}


class WordSearchII:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        if not board or m == 0 or n == 0:
            return []
        root = TrieNode()
        wset = set()

        def insertWord(word:str):
            node = root
            for ch in word:
                if ch not in node.links: #node.links[ord(ch)-ord('a')] is None:
                    node.links[ch] = TrieNode()
                node = node.links[ch]
            node.word = word

        def dfs(node: TrieNode, row:int, col:int):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] == '*':
                return
            ch = board[row][col]
            if ch not in node.links: #node.links[ord(ch)-ord('a')] is None:
                return
            node = node.links[ch]
            if node.word:
                wset.add(node.word)

            dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            board[row][col] = '*' #visited
            for r, c in dxy:
                dfs(node, row+r, col+c)
            board[row][col] = ch #Assign the original value back
            return

        for word in words:
            insertWord(word)

        for r, c in itertools.product(range(m), range(n)):
            dfs(root, r, c)

        return [w for w in wset]
