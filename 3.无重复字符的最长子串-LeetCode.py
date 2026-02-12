"""
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。



    示例 1:

    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
    示例 2:

    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:

    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            se : 记录集合
            rp : 右指针（初始值为-1表示未包含任何值）
            n : 字符串长度
            ans : 记录最长结果
        """
        se = set()
        rp = -1
        n = len(s)
        ans = 0

        for i in range(n):
            # 判定左指针(i)是否大于0，如果大于则表名窗口右移需移除前一个不在窗口中的元素
            if i > 0:
                se.remove(s[i - 1])

            """
                判定右指针(+1)是否比字符串小且指向元素是否不在集合中
                是，则记录元素并右移右指针
                否，则跳出while判断
            """
            while rp + 1 < n and s[rp + 1] not in se:
                se.add(s[rp + 1])
                rp += 1

            # 比较获得的集合长度和已有的集合长度，取最大值
            ans = max(ans, rp - i + 1)
        return ans