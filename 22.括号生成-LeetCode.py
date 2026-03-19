"""
    数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



    示例 1：

    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]
    示例 2：

    输入：n = 1
    输出：["()"]
"""
# 暴力递归
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 先定义有效括号
        def valid(A):
            count = 0
            for c in A:
                if c == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0: return False
            return count == 0

        def generate(A):
            if len(A) == 2 * n:         # 有效括号组长度必然为2n
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')       # 当n=2时这里可以理解为(((( -> ((() -> (()( -> (()) ... 的二进制加法
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        ans = []
        generate([])        # 这里给初始A = []
        return ans

# 回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:        # 当n=3时这里可以理解为((())) -> (()()) -> (())() -> ()(()) -> ()()()，每次移除到除上一轮最外层左括号后补上右括号，每轮优先补左括号
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        ans = []
        backtrack([], 0, 0)
        return ans
