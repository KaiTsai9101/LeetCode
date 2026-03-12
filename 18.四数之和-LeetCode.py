"""
    给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

    0 <= a, b, c, d < n
    a、b、c 和 d 互不相同
    nums[a] + nums[b] + nums[c] + nums[d] == target
    你可以按 任意顺序 返回答案 。



    示例 1：

    输入：nums = [1,0,-1,0,-2,2], target = 0
    输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    示例 2：

    输入：nums = [2,2,2,2,2], target = 8
    输出：[[2,2,2,2]]
"""
# 暴力求解
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = n - 1
                while d > c:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        # 去重（去完重后索引还是指向后一个重复的所以之后还要c+=1,d-=1）
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        # 这里可以一起移动索引因为只移动一个如果total还是等于target只有可能还是原来的结果值
                        c += 1
                        d -= 1
                    elif total > target:
                        d -= 1
                    else:
                        c += 1
        return res