"""
URL : https://leetcode.com/explore/interview/card/amazon/81/design/3000/
"""
from operator import itemgetter


# Brute Force
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.history = {}
        self.current_word = ''
        for i in range(len(sentences)):
            self.history[sentences[i]] = times[i]

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        output = []

        if c == '#':
            self.history.update({self.current_word: self.history.get(self.current_word, 0) + 1})
            self.current_word = ''
        else:
            result = []
            self.current_word += c

            for key in self.history.keys():
                if key[:len(self.current_word)] == self.current_word:
                    result.append((key, self.history[key]))

            temp = sorted(result, key=itemgetter(0))
            result = sorted(temp, key=itemgetter(1), reverse=True)

            for i in range(min(3, len(result))):
                output.append(result[i][0])
        return output


# Using Trie
class TrieNode:
    def __init__(self, st):
        self.sentence = st
        self.times = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word, times):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode(w)
            node = node.children[w]
        node.times += times

    def _startsWith(self, prefix):
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return None
        return node

    def _traverse(self, node, word, word_list):
        if node.times > 0:
            word_list.append((word, node.times))

        for key, value in node.children.items():
            self._traverse(node.children[key], word + key, word_list)

    def lookup(self, word):
        word_list = []
        node = self._startsWith(word)

        if node:
            self._traverse(node, word, word_list)
            return word_list
        else:
            return []


class AutocompleteSystem2:
    def __init__(self, sentences, times):
        self.trie = Trie()
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
        self.current_word = ''

    def input(self, c):
        output = []

        if c == '#':
            self.trie.insert(self.current_word, 1)
            self.current_word = ''
        else:
            self.current_word += c

            result = self.trie.lookup(self.current_word)

            temp = sorted(result, key=itemgetter(0))
            result = sorted(temp, key=itemgetter(1), reverse=True)

            for i in range(min(3, len(result))):
                output.append(result[i][0])
        return output


sentences = ["island", "i love you","ironman", "i love leetcode"]
times = [3, 5, 2, 2]
obj = AutocompleteSystem2(sentences, times)
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
print(obj.input('i'))
print(obj.input(' '))
print(obj.input('a'))
print(obj.input('#'))
