"""
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

    注意：答案中不可以包含重复的三元组。





    示例 1：

    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]
    解释：
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
    不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
    注意，输出的顺序和三元组的顺序并不重要。
    示例 2：

    输入：nums = [0,1,1]
    输出：[]
    解释：唯一可能的三元组和不为 0 。
    示例 3：

    输入：nums = [0,0,0]
    输出：[[0,0,0]]
    解释：唯一可能的三元组和为 0 。
"""
# 暴力求解
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        seen = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if triplet not in seen:
                            """
                                这里如果尝试写成 seen = seen.add(triplet)，那么 seen 就会变成 None，下次再使用 seen 就会报错！
                                Python中很多修改对象的方法都遵循"就地修改"原则，返回None：
                                list.append()、list.extend()、list.sort()、set.add()、set.update()、dict.update()
                            """
                            seen.add(triplet)
                            result.append([nums[i], nums[j], nums[k]])


        return result
