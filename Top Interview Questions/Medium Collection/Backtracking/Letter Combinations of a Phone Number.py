"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/
"""


class Solution(object):
    def is_a_solution(self, step, length):
        return step == length

    def construct_candidates(self, step, input, candidates, digits_to_letters):
        for alpha in digits_to_letters[input[step-1]]:
            candidates.append(alpha)

    def backtrack(self, answer, step, input, output, digits_to_letters):
        candidates = []

        if self.is_a_solution(step, len(input)):
            output.append(''.join(answer))
        else:
            step += 1
            self.construct_candidates(step, input, candidates, digits_to_letters)
            for i in range(len(candidates)):
                answer[step-1] = candidates[i]
                self.backtrack(answer, step, input, output, digits_to_letters)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        digit_to_letters = {
            '2': ["a", "b", "c"],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        output = []
        answer = [0] * (len(digits))

        self.backtrack(answer, 0, digits, output, digit_to_letters)

        return output
