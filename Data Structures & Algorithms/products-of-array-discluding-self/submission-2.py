class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #smart solution
        n = len(nums)

        sol = [3]*n
        prefix = 1
        for i in range(n):
            sol[i] = prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            sol[i]*= postfix
            postfix*= nums[i]
        return sol
