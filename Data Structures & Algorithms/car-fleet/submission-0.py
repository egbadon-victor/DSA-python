class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        t_pos = []
        fleets = 1
        t_stack = []

        for i, p in enumerate(position):
            t_pos.append((p,i))
        
        t_pos.sort(reverse=True)

        for (pos, i) in t_pos:
            t = (target - pos) / speed[i]
            if t_stack and t > t_stack[0]:
                t_stack.clear()
                fleets += 1
            t_stack.append(t)

        return fleets




