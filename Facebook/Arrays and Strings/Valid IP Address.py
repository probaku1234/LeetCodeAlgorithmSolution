"""
URL : https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3018/
"""


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        i = IP.find('.')
        j = IP.find(':')

        if i != -1 and j != -1:
            return "Neither"
        elif i != -1:
            string_list = IP.split('.')
            if len(string_list) != 4:
                return 'Neither'
            for string in string_list:
                if string == '':
                    return 'Neither'
                if string[0] == '0' and len(string) != 1:
                    return 'Neither'
                if not string.isnumeric():
                    return 'Neither'
                number = int(string)
                if number < 0 or number > 255:
                    return 'Neither'
            return 'IPv4'
        else:
            string_list = IP.split(':')
            if len(string_list) != 8:
                return 'Neither'

            hex_string = '0123456789abcdefABCDEF'
            for digits in string_list:
                if len(digits) > 4 or len(digits) == 0:
                    return 'Neither'
                for letter in digits:
                    if letter not in hex_string:
                        return 'Neither'

            return 'IPv6'

print(Solution().validIPAddress('192.0.0.1'))