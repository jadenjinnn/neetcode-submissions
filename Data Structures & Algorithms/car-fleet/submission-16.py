class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append([position[i], (target-position[i])/speed[i]])

        cars.sort(key=lambda x:x[0], reverse=True)

        stack = []

        for car in cars:
            if not stack:
                stack.append(car)
            else:
                if not (stack[-1][0]>=car[0] and car[1] <= stack[-1][1]): 
                    stack.append(car)

        return len(stack)