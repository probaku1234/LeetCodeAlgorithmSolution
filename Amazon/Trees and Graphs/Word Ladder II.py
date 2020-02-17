"""
URL : https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/483/
"""
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(set)

    def add_edges(self, v, w):
        self.graph[v].add(w)
        self.graph[w].add(v)

    def bfs(self, start, end, result):
        visited = {start}
        found = False
        trace = defaultdict(list)
        trace[start] = []

        queue = [start]

        while queue:
            s = queue.pop(0)

            for neighbor in self.graph[s]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    trace[neighbor].append(s)
                    if neighbor == end:
                        found = True
        #print(trace)
        if found:
            self.backtrack(result, trace, [], end)

    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)

class Solution(object):
    def helper(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1

        return count == 1

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        out = []

        if endWord not in wordList:
            return []

        word = beginWord
        n = len(wordList)
        g = Graph(n + 1)

        for i in range(n):
            for j in range(i, n):
                if word != wordList[j] and self.helper(word, wordList[j]):
                    g.add_edges(word, wordList[j])

            word = wordList[i]

        g.bfs(beginWord, endWord, out)
        return out

    def v2(self, start, end, dic):
        dic.add(start)
        dic.add(end)

        result, cur, visited, found, trace = [], [start], set([start]), False, {word: [] for word in dic}

        while cur and not found:
            for word in cur:
                visited.add(word)

            next_word = set()
            for word in cur:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dic:
                            if candidate == end:
                                found = True
                            next_word.add(candidate)
                            trace[candidate].append(word)
            cur = next_word
        #print(trace)
        if found:
            self.backtrack(result, trace, [], end)

        return result

    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)


print(Solution().findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
print(Solution().findLadders('a', 'c', ['a', 'b', 'c']))
#print(Solution().v2('hit', 'cog', set(["hot","dot","dog","lot","log","cog"])))
#print(Solution().v2('a', 'c', set(['a', 'b', 'c'])))