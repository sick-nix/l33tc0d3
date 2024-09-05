from typing import List


class RecentCounter:
    request: List[int] = []
    low_bound: int = 0

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)

        if t <= 3000:
            i = 0
        else:
            low_bound = t - 3000
            i = self.low_bound
            while self.requests[i] < low_bound:
                i += 1
            self.low_bound = i

        return len(self.requests) - i

    # Your RecentCounter object will be instantiated and called as such:
    # obj = RecentCounter()
    # param_1 = obj.ping(t)

    def process_pings(self, pings: List[List[int]]) -> List[int]:
        reqs = []

        for p in pings:
            if p == []:
                reqs.append(None)
            else:
                t = p[0]
                reqs.append(self.ping(t))

        return reqs
