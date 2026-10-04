class Solution:
    def mySqrt(self, x: int) -> int:
        one_less = 0
        one_more = 1

        # x = 13, where 3^2 = 9 and 4^2 = 16... need to find the closest int to the square root, meaning we need to check one before and one after

        # while one_more * one_more <= x:
            

        #     one_less+=1 
        #     one_more+=1

        # return one_less

        #answer must be less than x / 2... binary search

        low = 1
        high = x
        mid = 0
        current = 0
        while low <= high: 
            mid = (low + high)//2
            if mid * mid > x:
                high = mid-1
            else:
                current = mid
                low = mid+1

        return current