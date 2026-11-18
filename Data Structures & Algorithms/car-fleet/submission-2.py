class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        t_pos = sorted(zip(position, speed), reverse=True)

        fleets = 0
        lead_time = 0
        

        for pos, s in t_pos:
            t = (target - pos) / s
            if t > lead_time:
                fleets += 1
                lead_time = t

        return fleets




