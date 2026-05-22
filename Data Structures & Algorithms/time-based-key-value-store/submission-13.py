class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]

        l, r = 0, len(data)-1
        sol = ""

        while l<=r:
            mid = (l+r)//2

            if (data[mid][1]) > timestamp:
                r = mid-1
            else:
                sol = data[mid][0]
                l = mid+1
            
        return sol
