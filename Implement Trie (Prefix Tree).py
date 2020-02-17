"""
URL : https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self, k):
        self.v = 0
        self.k = k
        self.children = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(w)
            node = node.children[w]
        node.v += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self._startsWith(word)
        if node and node.v:
            return True
        else:
            return False

    def _startsWith(self, prefix):
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return None
        return node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if self._startsWith(prefix):
            return True
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)