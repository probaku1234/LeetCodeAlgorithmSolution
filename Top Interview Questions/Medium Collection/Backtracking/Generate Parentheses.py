"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
"""


class Solution(object):
    def is_valid(self, s):
        if len(s) == 0:
            return True

        stack = []

        for p in s:
            if p == '(':
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()

        return len(stack) == 0

    def is_a_solution(self, answer, step, n):
        if step == n * 2:
            return self.is_valid(''.join(answer))
        else:
            return False

    def process_solution(self, answer, output):
        output.append(''.join(answer))

    def construct_candidates(self, candidates):
        candidates[0] = '('
        candidates[1] = ')'

    def backtrack(self, answer, step, input, output):
        candidates = ['a'] * 2

        if self.is_a_solution(answer, step, input):
            self.process_solution(answer, output)
        else:
            step += 1
            if step > input * 2:
                return
            self.construct_candidates(candidates)
            for i in range(len(candidates)):
                answer[step-1] = candidates[i]
                self.backtrack(answer, step, input, output)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = ['a'] * (n * 2)
        output = []

        self.backtrack(answer, 0, n, output)

        return output


s = Solution()
print s.generateParenthesis(3)
