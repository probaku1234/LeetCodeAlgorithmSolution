from collections import defaultdict
import heapq

class MonitoringSystem:

    def __init__(self):
        self.app_api_to_latencies = defaultdict(list) # dictionary to store latencies of api
        self.app_api_to_errors_and_counts = defaultdict(lambda: defaultdict(int)) #
        self.app_to_apis = defaultdict(set) # set of api names in app


    def logLatency(self, applicationName: str, api: str, latencyInMills: int):
        self.app_api_to_latencies[(applicationName, api)].append(latencyInMills)
        self.app_to_apis[applicationName].add(api)


    def logError(self, applicationName: str, api: str, errorCode: int):
        self.app_api_to_errors_and_counts[(applicationName, api)][errorCode] += 1
        self.app_to_apis[applicationName].add(api)


    def getPercentileLatency(self, percentile: int, applicationName: str, api: str):
        latencies_for_app_api = self.app_api_to_latencies[(applicationName, api)]

        if latencies_for_app_api:
            index = max(0, (percentile * len(latencies_for_app_api) // 100) - 1)
            latencies_for_app_api.sort()
            return latencies_for_app_api[index]
        else:
            latencies_for_app = []
            for api in self.app_to_apis[applicationName]:
                latencies_for_app_api = self.app_api_to_latencies[(applicationName, api)]
                latencies_for_app += latencies_for_app_api

            latencies_for_app.sort()
            index = max(0, (percentile * len(latencies_for_app) // 100) - 1)
            return latencies_for_app[index]


    def getTopErrors(self, applicationName: str, api: str):
        app_api_errors = self.app_api_to_errors_and_counts[(applicationName, api)]
        # heapify creates min heap, we want max value so make negative number
        max_heap = [(-count, error_code) for error_code, count in app_api_errors.items()]
        # if there are less than 3, make all error list
        if len(max_heap) < 3:
            max_heap = []
            for api in self.app_to_apis[applicationName]:
                app_api_errors = self.app_api_to_errors_and_counts[(applicationName, api)]
                max_heap += [(-ct, error_code) for error_code, ct in app_api_errors.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(3)]
