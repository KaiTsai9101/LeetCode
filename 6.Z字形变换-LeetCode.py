"""
    将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

    比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

    P   A   H   N
    A P L S I I G
    Y   I   R
    之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

    请你实现这个将字符串进行指定行数变换的函数：

    string convert(string s, int numRows);
     

    示例 1：

    输入：s = "PAYPALISHIRING", numRows = 3
    输出："PAHNAPLSIIGYIR"
    示例 2：
    输入：s = "PAYPALISHIRING", numRows = 4
    输出："PINALSIGYAHRPI"
    解释：
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    示例 3：

    输入：s = "A", numRows = 1
    输出："A"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r, n = numRows, len(s)

        if r == 1 or r >= n:
            return s

        # 一个周期的字符个数
        t = r * 2 - 2
        # 结合一个周期的列数c = r - 1，推算总列数（向上取整）
        c = ((n + t - 1) // t) * (r - 1)

        # 创建一个r行c列的('')空矩阵
        m = [[''] * c for _ in range(r)]
        # 初始化x, y坐标
        x, y = 0, 0
        for i, ch in enumerate(s):
            m[x][y] = ch
            if i % t < r - 1:
                x += 1      # 坐标向下移动
            else:
                x -= 1
                y += 1      # 坐标向右上移动

        # 按照从上往下，从左往右返回不带空字符串的值
        return ''.join(ch for row in m for ch in row if ch)
        """
            ''.join:表示将字符根据''内容连接

            # python的生成器表达式语法
            ch for row in m for ch in row if ch

            # 等效于
            chars = []
            for row in m:           # 将矩阵按行划分
                for ch in row:          # 将行按字划分
                    if ch:          # 当字符为真将字符写进chars数组
                        chars.append(ch)
            return ''.join(chars)           # 将得到的char数组连接，连接符号为''
        """