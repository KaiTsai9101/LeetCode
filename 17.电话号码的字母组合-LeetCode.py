"""
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


    示例 1：

    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
    示例 2：

    输入：digits = "2"
"""
# 暴力求解（三层循环）
class Solution:
    def letterCombinations(self, digits: str):
        dic = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = [""]

        # digits = "234"，三层循环
        for n in digits:        # 第一层循环，控制处理哪个数字位
            res = [x + y for x in res for y in dic[n]]
            """
                new_res = [""]
                for x in res:       # 第二层循环，取出已有的每种组合（初始是[""]）
                    for y in hash_n_to_c[n]:        # 第三层循环，与当前数字的每个可能字母组合
                        new_res.append(x + y)
                res = new_res
            """
        return res

# 回溯法求解
class Solution:
    def letterCombinations(self, digits: str):
        dic = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        if not digits:
            return list()

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))       # 把每次得到的最深combination结果输出
            else:
                # digits = "234"
                digit = digits[index]
                for letter in dic[digit]:       # 每一次递归都只会在当前位数做改变（append和pop）
                    combination.append(letter)
                    backtrack(index + 1)        # 递归调用
                    combination.pop()

        combination = []
        combinations = []
        backtrack(0)

        return combinations
