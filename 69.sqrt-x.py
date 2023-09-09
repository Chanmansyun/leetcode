#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        while (mid:=(low+high)//2) != low:
            if mid**2 > x:
                high = mid
            elif mid**2 < x:
                low = mid
            else:
                return mid
        return low
        
# @lc code=end

