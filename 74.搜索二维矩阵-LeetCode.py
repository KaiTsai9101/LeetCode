"""
    给你一个满足下述两条属性的 m x n 整数矩阵：

    每行中的整数从左到右按非严格递增顺序排列。
    每行的第一个整数大于前一行的最后一个整数。
    给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。



    示例 1：


    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    输出：true
    示例 2：


    输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    输出：false
"""
# 暴力求解
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:     # 这里不能if target == i因为i为matrix的其中一行，按行遍历，所以只能查询target是不是在当前行中
                return True
        return False

# 二分法求解
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        if h == 0:
            return False
        w = len(matrix[0])
        if w == 0:
            return False

        left = 0
        right = w * h - 1

        while left <= right:
            mid = (left + right) // 2  # 3x4矩阵，mid == 5 -> 应该要在第1行第1列
            i = mid // w
            j = mid % w

            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                left = mid + 1
            else:
                right = mid - 1
        return False