"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []

        for p in s:
            if p == '[' or p == '{' or p == '(':
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                if p == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if p == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if p == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0