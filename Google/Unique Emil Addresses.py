"""
URL : https://leetcode.com/explore/featured/card/google/67/sql-2/3044/
"""

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if len(emails) == 1:
            return 1

        email_dict = {}
        count = 0

        for email in emails:
            string_list = email.split('@')
            string_list[0] = string_list[0].replace('.','')
            index = string_list[0].find('+')
            if index > -1:
                string_list[0] = string_list[0][:index]
            if email_dict.get(string_list[1]) is None:
                email_dict[string_list[1]] = {string_list[0]}
            else:
                email_dict[string_list[1]].add(string_list[0])

        for value in email_dict.values():
            count += len(value)

        return count
