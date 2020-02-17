"""
URL : https://leetcode.com/explore/interview/card/amazon/81/design/3000/
"""
from operator import itemgetter


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


sentences = ["island", "i love you","ironman", "i love leetcode"]
times = [3,5,2,2]
obj = AutocompleteSystem(sentences, times)
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
