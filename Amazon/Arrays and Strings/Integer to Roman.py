"""
URL : https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2964/
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ''
        int_to_roman_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        num_string = str(num)
        n = len(num_string)

        for i in range(n):
            if num_string[i] == '0':
                continue
            number = int(num_string[i])

            if int_to_roman_dict.get(number * (10 ** (n - i - 1))) is not None:
                output += int_to_roman_dict[number * (10 ** (n - i - 1))]
            elif number < 4:
                for j in range(int(num_string[i])):
                    output += int_to_roman_dict[10 ** (n - i - 1)]
            elif number > 5:
                output += int_to_roman_dict[5 * (10 ** (n - i - 1))]
                for j in range(int(num_string[i]) - 5):
                    output += int_to_roman_dict[10 ** (n - i - 1)]

        return output


print(Solution().intToRoman(3000))
print(Solution().intToRoman(80))