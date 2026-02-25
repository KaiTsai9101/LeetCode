"""
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    例如，121 是回文，而 123 不是。


    示例 1：

    输入：x = 121
    输出：true
    示例 2：

    输入：x = -121
    输出：false
    解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
    示例 3：

    输入：x = 10
    输出：false
    解释：从右向左读, 为 01 。因此它不是一个回文数。
"""
# 暴力解
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 将字符由整数型转换成字符型，并使其与其倒序进行比较后返回布尔结果
        return str(x) == str(x)[::-1]

# 反转一半数字
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 当x为负数或当x不为0时的个位数不为0   # -121 != 121-  || 10 != 01
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        """
            例：x=1221
            while循环后: x == 12, reversed_half == 12  # 满足 x == reversed_half
            例：x=121
            while循环后: x == 1, reversed_half == 12   # 满足 x == reversed_half // 10（当数字为奇数位时中间数字不影响是否为回文子串）
        """
        return x == reversed_half or x == reversed_half // 10

# 完全反转数字
INT_MAX = 2 ** 31 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original = x
        reversed_num = 0

        while x > 0:
            # 判断边界，反转后的数不能超过最大边界
            if reversed_num > INT_MAX:
                return False

            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        return original == reversed_num