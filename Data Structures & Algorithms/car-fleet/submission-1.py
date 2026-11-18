class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        t_pos = list(zip(position, speed))
        fleets = 1
        t_stack = []
        
        t_pos.sort(reverse=True)

        for (pos, s) in t_pos:
            t = (target - pos) / s
            if t_stack and t > t_stack[0]:
                t_stack.clear()
                fleets += 1
            t_stack.append(t)

        return fleets




