"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
"""


class Solution(object):
    def is_a_solution(self, step, n):
        return step == n

    def process_solution(self, answer, step, input, output):
        temp = []

        for i in range(step):
            if answer[i]:
                temp.append(input[i])

        output.append(temp)

    def construct_candidates(self,candidates):
        candidates[0] = True
        candidates[1] = False

    def backtrack(self, answer, step, input, output):
        candidates = [False] * 2

        if self.is_a_solution(step, len(input)):
            self.process_solution(answer, step, input, output)
        else:
            step += 1
            self.construct_candidates(candidates)
            for i in range(len(candidates)):
                answer[step-1] = candidates[i]
                self.backtrack(answer, step, input, output)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = ['a'] * len(nums)
        output = []

        self.backtrack(answer, 0, nums, output)

        return output
