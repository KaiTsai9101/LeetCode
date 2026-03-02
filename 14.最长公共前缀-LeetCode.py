"""
    编写一个函数来查找字符串数组中的最长公共前缀。

    如果不存在公共前缀，返回空字符串 ""。



    示例 1：

    输入：strs = ["flower","flow","flight"]
    输出："fl"
    示例 2：

    输入：strs = ["dog","racecar","car"]
    输出：""
    解释：输入不存在公共前缀。
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 当strs为空或长度为0时返回空字符串
        if not strs:
            return ""

        prefix, value = 0, strs[0]
        n = len(strs)

        for i in range(1, n):
            """
                创建一个临时最长公共字符串strs[prefix]
                初始将第0号字符串设为临时最长公共字符串并跟第1号字符串比较
                将二者的最长公共前缀赋值给最长公共字符串，并继续循环跟之后的字符串比较
                最终返回最长公共前缀
            """
            value = self.lcp(strs[prefix], strs[i])
            strs[prefix] = value

            # 如果比较期间已经没有公共字符串则不用继续跟后续字符串比较，直接返回空字符串
            if not strs:
                return ""

        return value

    def lcp(self, str1, str2):
        # 将短的字符串长度设为边界
        length, index = min(len(str1), len(str2)), 0

        """
            默认从字符串的第0号元素开始比较
            若元素下标小于短字符串长度且两个元素值相同则下标右移继续比较下一个元素下标的值
            最后返回得到的字符串切片[0-下标（不含下标值））
        """
        while index < length and str1[index] == str2[index]:
            index += 1

        return str1[:index]