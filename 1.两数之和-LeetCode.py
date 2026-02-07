"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""

# 暴力求解
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 优化算法（创建hash表）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

"""
    num = [2, 7, 11, 15]
    target = 9
    hashtable = {}
    
    enumerate(items, start)为遍历start和item的值，默认start为0，递增
    0 2
    1 7
    2 11
    3 15
    
    第一轮循环: i = 0, num = 2, hashtable = {}
    target - num in hashtable       # if 9-2 in {} -> False
    hashtable[nums[i]] = i          # hashtable = {2:0}
    
    第二轮循环: i = 1, num = 7, hashtable = {2:0}
    ** for...in对字典的操作：检查键是否存在，不关系值
    target - num in hashtable       # if 9-7 in {2:0} -> True
    进入if语句，返回[hashtable[2], 1] -> [0, 1]
"""