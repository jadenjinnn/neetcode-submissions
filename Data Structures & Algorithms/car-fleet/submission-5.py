class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        
        for i in range(len(position)):
            cars.append((position[i], (target-position[i])/speed[i]))


        cars.sort(key=lambda x:x[0], reverse=True)
        print(cars)

        fleets = 0
        stack = []

        for car in cars:
            if not stack:
                stack.append(car)
            else:
                if stack[-1][1] < car[1]:
                    stack.append(car)
                
            
        return len(stack)
            