"""
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    每个右括号都有一个对应的相同类型的左括号。


    示例 1：

    输入：s = "()"

    输出：true

    示例 2：

    输入：s = "()[]{}"

    输出：true

    示例 3：

    输入：s = "(]"

    输出：false

    示例 4：

    输入：s = "([])"

    输出：true

    示例 5：

    输入：s = "([)]"

    输出：false
"""
# 栈求解
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        left_signed = ["(", "[", "{"]
        stack = []

        # 如果字符串长度为奇数则一定有无法配对的字符
        if len(s) % 2 == 1:
            return False

        for ch in s:
            if ch in left_signed:       # 所有左括号字符放入栈中
                stack.append(ch)
            else:
                if not stack or stack[-1] != dict[ch]:      # 如果栈空（没有任何字符传入过）或者当栈顶元素!=当前字符键对应的值返回False
                    return False
                stack.pop()     # 找到对应的右括号字符，将栈顶元素弹出
        return len(stack) == 0      # 确保所有左字符都有对应的右字符（即最后栈长度为0）