class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i], (target-position[i])/speed[i]))

        cars.sort(key=lambda x:x[0], reverse=True)
        print(cars)
        stack = []

        for pos, time in cars:
            if not stack:
                stack.append((pos, time))
            elif stack[-1][1] < time:
                stack.append((pos, time))

        return len(stack)