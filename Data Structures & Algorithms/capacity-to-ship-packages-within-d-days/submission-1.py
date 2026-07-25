class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights) , sum(weights)
        res = r


        def can_ship(cap):
            ships , curcap = 1 , cap
            for w in weights:
                if curcap - w < 0 :
                    ships += 1
                    curcap = cap
                curcap = curcap - w
            return ships <=days


        while l<=r:
            mid = (l+r)//2

            if can_ship(mid):
                res = min(res,mid)
                r = mid -1
            else:
                l = mid + 1
        return res
        