class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.keys[key])-1
        res = ""

        while l<=r:
            mid = l + (r-l) // 2
            
            if timestamp >= self.keys[key][mid][0]:
                l = mid +1
                res =  self.keys[key][mid][1]
            elif timestamp < self.keys[key][mid][0]:
                r = mid-1
                
        return res
