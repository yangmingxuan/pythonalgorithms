class TrieNode(object):
    links = None

    def __init__(self):
        self.links = [TrieNode()] * 26

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch)-ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
