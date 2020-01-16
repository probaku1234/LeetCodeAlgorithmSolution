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
        int_to_roman_dict_one = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX'
        }
        int_to_roman_dict_two = {
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC'
        }
        int_to_roman_dict_three = {
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM'
        }
        int_to_roman_dict_four = {
            1000: 'M'
        }
        dict_list = [int_to_roman_dict_one, int_to_roman_dict_two, int_to_roman_dict_three, int_to_roman_dict_four]
        num_string = str(num)
        n = len(num_string)

        for i in range(n):
            if num_string[i] == '0':
                continue
            number = int(num_string[i]) * (10 ** (n - i - 1))
            num_dict = dict_list[n - i - 1]

            if num_dict.get(number) is not None:
                output += num_dict[number]
            elif number < 4 * (10 ** (n - i - 1)):
                for j in range(int(num_string[i])):
                    output += num_dict[10 ** (n - i - 1)]
            elif number > 5 * (10 ** (n - i - 1)):
                output += num_dict[5 * (10 ** (n - i - 1))]
                for j in range(int(num_string[i]) - 5):
                    output += num_dict[10 ** (n - i - 1)]

        return output


print(Solution().intToRoman(3000))
print(Solution().intToRoman(80))