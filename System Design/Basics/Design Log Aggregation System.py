"""
https://leetcode.com/explore/featured/card/system-design/689/system-design-basics/4406/
"""

from collections import defaultdict

class LogAggregator:

    def __init__(self, machines: int, services: int):
        self.machineLog = defaultdict(list)
        self.serviceLog = defaultdict(list)

    def pushLog(self, logId: int, machineId: int, serviceId: int, message: str) -> None:
        self.machineLog[machineId].append((logId, serviceId, message))
        self.serviceLog[serviceId].append((logId, machineId, message))

    def getLogsFromMachine(self, machineId: int):
        res = []
        for log in self.machineLog[machineId]:
            res.append(log[0])
        return res


    def getLogsOfService(self, serviceId: int):
        res = []
        for log in self.serviceLog[serviceId]:
            res.append(log[0])
        return res

    def search(self, serviceId: int, searchString: str):
        res = []
        for log in self.serviceLog[serviceId]:
            if searchString in log[2]:
                res.append(log[2])

        return res

# Your LogAggregator object will be instantiated and called as such:
logAggregator = LogAggregator(3, 3)
logAggregator.pushLog(2322, 1, 1, "Machine 1 Service 1 Log 1")
logAggregator.pushLog(2312, 1, 1, "Machine 1 Service 1 Log 2")
logAggregator.pushLog(2352, 1, 1, "Machine 1 Service 1 Log 3")
logAggregator.pushLog(2298, 1, 1, "Machine 1 Service 1 Log 4")
logAggregator.pushLog(23221, 1, 2, "Machine 1 Service 2 Log 1")
logAggregator.pushLog(23121, 1, 2, "Machine 1 Service 2 Log 2")
logAggregator.pushLog(23222, 2, 2, "Machine 2 Service 2 Log 1")
logAggregator.pushLog(23122, 2, 2, "Machine 2 Service 2 Log 2")
logAggregator.pushLog(23521, 1, 2, "Machine 1 Service 2 Log 3")
logAggregator.pushLog(22981, 1, 2, "Machine 1 Service 2 Log 4")
logAggregator.pushLog(23522, 2, 2, "Machine 2 Service 2 Log 3")
logAggregator.pushLog(22982, 2, 2, "Machine 2 Service 2 Log 4")
logAggregator.getLogsFromMachine(2)
logAggregator.getLogsOfService(2)
a = logAggregator.search(1, "Log 1")
b = logAggregator.search(2, "Log 3")
print(a)
print(b)