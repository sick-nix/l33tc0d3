from solution import RecentCounter

o = RecentCounter()

assert o.process_pings([[], [1], [100], [3001], [3002]]) == [None, 1, 2, 3, 3]
