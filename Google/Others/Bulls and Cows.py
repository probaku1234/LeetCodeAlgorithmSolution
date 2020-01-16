"""
URL : https://leetcode.com/explore/interview/card/google/66/others-4/3100/
"""
from collections import defaultdict, Counter


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_a, num_b = 0, 0
        secret_dict = defaultdict(list)
        guess_dict = defaultdict(list)

        for i in range(len(secret)):
            secret_dict[secret[i]].append(i)
            guess_dict[guess[i]].append(i)

        for k, v in guess_dict.items():
            if k in secret_dict.keys():
                count = 0
                for index in v:
                    if index in secret_dict[k]:
                        num_a += 1
                        count += 1

                if len(v) - count > 0:
                    if len(secret_dict[k]) - count > 0:
                        num_b += min(len(secret_dict[k]) - count, len(v) - count)

        return str(num_a) + 'A' + str(num_b) + 'B'

    def v2(self, secret, guess):
        guess = list(guess)
        secret = list(secret)
        counter = Counter(secret)
        a_count = 0
        b_count = 0

        for i in range(len(guess)):
            if guess[i] == secret[i]:
                counter[guess[i]] -= 1
                guess[i] = 'A'
                secret[i] = 'A'
                a_count += 1

        for i in range(len(guess)):
            if guess[i] != 'A' and counter[guess[i]] > 0:
                counter[guess[i]] -= 1
                guess[i] = 'B'
                b_count += 1

        return str(a_count) + 'A' + str(b_count) + 'B'

print(Solution().v2("1122", '0001'))