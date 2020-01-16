"""
URL : https://leetcode.com/explore/interview/card/google/65/design-4/3093/
"""


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        time = self.messages.get(message, -1)

        if time == -1:
            self.messages[message] = timestamp
            return True
        if timestamp - time >= 10:
            self.messages[message] = timestamp
            return True
        else:
            return False


logger = Logger()
print(logger.shouldPrintMessage(0, "A"))
print(logger.shouldPrintMessage(0, "B"))
print(logger.shouldPrintMessage(0, "C"))
print(logger.shouldPrintMessage(0, "A"))
print(logger.shouldPrintMessage(0, "B"))
print(logger.shouldPrintMessage(0, "C"))
