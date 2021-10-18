class TrieNode(object):
    links = None
    word:str = None
    is_end:bool = False

    def __init__(self):
        self.links = [None] * 26

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch)-ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.is_end = True

    def isEnd(self) -> bool:
        return self.is_end

    def setWord(self, text:str):
        self.word = text

    def getWord(self) -> str:
        return self.word
