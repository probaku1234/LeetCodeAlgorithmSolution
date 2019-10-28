"""
URL : https://leetcode.com/explore/interview/card/google/59/array-and-strings/3051/
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        array = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                array[i+j] += int(num1[i]) * int(num2[j])

        ans = []
        for i in range(len(array)):
            digit = array[i] % 10
            carry = array[i] // 10
            if i < len(array)-1:
                array[i+1] += carry
            ans.insert(0, str(digit))

        while ans[0] == '0' and len(ans) > 1:
            del ans[0]

        return ''.join(ans)

    def multiply2(self, num1, num2):
        n1 = n2 = 0
        if num1 == '0' or num2 == '0':
            return '0'

        for i in num1:
            n1 = (n1*10) + ord(i) - 48
        for i in num2:
            n2 = (n2*10) + ord(i) - 48
        return str(n1 * n2)
print(Solution().multiply2('3', '4'))
