"""
    给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。

    返回这三个数的和。

    假定每组输入只存在恰好一个解。



    示例 1：

    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
    示例 2：

    输入：nums = [0,0,0], target = 1
    输出：0
    解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        """
            因为nums[i]范围在-1000~1000，target在-10**4~10**4
            所以best要设置为大于13000才会使第一个ans一定记录到best中
            （当nums[a],nums[b],nums[c]均为-1000，且target为10000时：abs(3*-1000 - 10000)）
        """
        best = 10 ** 5

        def update(ans):
            nonlocal best   # 因为每次都要更改全局best值所以这里要nonlocal
            if abs(ans - target) < abs(best - target):
                best = ans

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b, c = a + 1, n - 1
            # target:5 nums=[0,1,2,3,4,5]
            while b < c:
                ans = nums[a] + nums[b] + nums[c]
                if ans == target:
                    return ans

                update(ans)     # 这里不管if，else都要用update方法，所以方法代码可以写在外面
                if ans > target:
                    c0 = c - 1      # 这里额外判断当c与上一个c相同值时跳过此次判断（不重复判断）
                    while b < c0 and nums[c0] == nums[c]:
                        c0 -= 1
                    c = c0
                else:
                    b0 = b + 1      # 这里额外判断当b与上一个b相同值时跳过此次判断（不重复判断）
                    while b0 < c and nums[b0] == nums[b]:
                        b0 += 1
                    b = b0

        return best     # 这里return要对好，对的是最外层循环