"""
Implement the MapSum class:

MapSum() Initializes the MapSum object.
void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""
from trie.TrieNode import TrieNode


class MapSum:

    def __init__(self):
        self.map = dict()
        self.root = TrieNodeSum()


    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.setdefault(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for c in key:
            if not cur.containsKey(c):
                cur.put(c, TrieNodeSum())
            cur = cur.get(c)
            cur.score += delta


    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            cur = cur.get(c)
            if not cur:
                return 0

        return cur.score

"""
class TrieNodeSum(TrieNode):
    score:int

    def __init__(self):
        TrieNode.__init__()
        self.score = 0
"""
class TrieNodeSum:
    score: int
    links = None

    def __init__(self):
        self.score = 0
        self.links = [None] * 26

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        return self.links[ord(ch)-ord('a')]

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

