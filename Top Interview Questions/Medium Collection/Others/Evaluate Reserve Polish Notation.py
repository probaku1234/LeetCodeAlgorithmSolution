"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/823/
"""


class Solution(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        return int(a / b)

    def multiple(self, a, b):
        return a * b

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        index = 0
        operators = {'+': self.add, '-': self.subtract, '/': self.divide, '*': self.multiple}

        while index < len(tokens):
            if tokens[index] == '+' or tokens[index] == '-' or tokens[index] == '/' or tokens[index] == '*':
                operator = tokens[index]
                first = int(tokens[index-2])
                second = int(tokens[index-1])
                result = operators[operator](first, second)
                tokens.insert(index-2, str(result))
                tokens.pop(index-1)
                tokens.pop(index-1)
                tokens.pop(index-1)
                index = index - 1
            else:
                index += 1

        return tokens[0]
