class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []

        for i in range(len(position)):
            cars.append((position[i], (target-position[i])/speed[i]))

        cars.sort(reverse=True)

        for p, s in cars:
            if not stack:
                stack.append((p,s))
            elif not (p<stack[-1][0] and s<=stack[-1][1]):
                stack.append((p,s))

        return len(stack)