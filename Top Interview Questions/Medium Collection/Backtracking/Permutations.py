"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/
"""
import copy

class Solution(object):
    def is_solution(self, step, length):
        return step == length

    def process_solution(self, answer, output):
        temp = copy.deepcopy(answer)
        output.append(temp)

    def construct_candidates(self, answer, step, input, candidates):
        in_perm = {num: False for num in input}

        for i in range(step):
            if answer[i] != 'a':
                in_perm[answer[i]] = True

        for key, value in in_perm.items():
            if not value:
                candidates.append(key)

    def backtrack(self, answer, step, input, output):
        candidates = []

        if self.is_solution(step, len(input)):
            self.process_solution(answer, output)
        else:
            step += 1
            self.construct_candidates(answer, step, input, candidates)
            for i in range(len(candidates)):
                answer[step-1] = candidates[i]
                self.backtrack(answer, step, input, output)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        answer = ['a'] * len(nums)
        output = []

        self.backtrack(answer, 0, nums, output)

        return output


s = Solution()
print s.permute([1,2,4])