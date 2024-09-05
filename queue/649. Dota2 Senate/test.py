from solution import Solution

o = Solution()

assert o.predictPartyVictory("RD") == "Radiant"
assert o.predictPartyVictory("RDD") == "Dire"
assert o.predictPartyVictory("RDR") == "Radiant"
assert o.predictPartyVictory("DDRRR") == "Dire"
