"""
    给你一个字符串 s，找到 s 中最长的 回文 子串。



    示例 1：

    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。
    示例 2：

    输入：s = "cbbd"
    输出："bb"
"""

# 动态规划算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # 当字符串长度为1时必为回文子串，直接输出
        if n == 1:
            return s

        max_len = 1
        begin = 0

        # 创建n * n二维数组，初始值全部设为False
        """
            [False] * n == [False, ..., False](n个False)
            [[False] * n for _ in range(n)] ==  [False, ..., False](n个False)
                                                ...                (n列False)
                                                [False, ..., False](n个False)
        """
        dp = [[False] * n for _ in range(n)]
        # 对角设为True（i开始i结束即长度为1必为回文子串）
        for i in range(n):
            dp[i][i] = True

        # 从长度为2开始循环（因为range默认0开始不算结束值所以n+1）
        for L in range(2, n + 1):
            for i in range(n):
                # 由L = j - i + 1反推得j = L + i - 1
                j = L + i - 1
                if j >= n:
                    break

                # 最外层2个字不相同则为False
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 当长度小于等于3时，最外层2个字相同则必为回文子串
                    if L <= 3:
                        dp[i][j] = True
                    # 当长度大于3时，最外层2个字相同后判断次外层两个字，依次判断直到长度小于3
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 比较最长回文子串并记录起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        # 返回起始位置开始的最长回文子串数组切片
        return s[begin:max_len + begin]

# 中心扩散算法
class Solution:
    # 中心扩散函数，只输出回文子串
    def expandAroundCenter(self, s, left, right):
        n = len(s)
        # 设置左右指针范围，且左右指针指的值相等才移动指针
        while left >= 0 and right < n and s[right] == s[left]:
            left -= 1
            right += 1
        """
            一直判断到不满足条件则返回上一个判断时的左右指针位置并输出
            # 上一个指针盘对为真才回到此判断
            # 此时left -= 1, right += 1所以要给left + 1, right - 1后才能输出
        """
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0

        for i in range(n):
            """
                通过函数筛选出来的回文子串选出最长回文子串
                需要对给定字符串是奇数还是偶数分别判定
            """
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        # 返回最长回文子串，因为数组不会截取最后一个元素所以end + 1
        return s[start: end + 1]