class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = list(senate)
        dbanned = 0
        rbanned = 0

        while True:
            if "D" not in queue:
                return "Radiant"
            if "R" not in queue:
                return "Dire"

            current = queue.pop(0)
            if current == "R":
                if rbanned > 0:
                    rbanned -= 1
                else:
                    dbanned += 1
                    queue.append(current)
            else:
                if dbanned > 0:
                    dbanned -= 1
                else:
                    rbanned += 1
                    queue.append(current)
