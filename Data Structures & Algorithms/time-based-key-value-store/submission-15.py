class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        sol = ""
        values = self.times[key]

        l, r = 0, len(values)-1

        while l<=r:
            mid = (l+r)//2

            if values[mid][1]>timestamp:
                r = mid-1
            else:
                l = mid+1
                sol = values[mid][0]

        return sol
