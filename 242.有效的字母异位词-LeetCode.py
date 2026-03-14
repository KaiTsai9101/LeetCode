"""
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。



    示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:

    输入: s = "rat", t = "car"
    输出: false
"""
# 暴力求解
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = list(t)    # 字符串不能拆解（之后会用到pop）所以这里先改成list

        for i in range(len(s)):
            j = 0
            while j < len(t_list):
                if j == len(t_list) - 1 and t_list[j] != s[i]:      # 当j指到列表t的最后一个元素还不相等时直接返回False
                    return False

                if t_list[j] == s[i]:       # 当有相同元素时将列表t的对应值弹出（防止重复检索）
                    t_list.pop(j)
                    break
                else:               # 不是相同元素则j索引向右移动
                    j += 1

        return True

# 排序
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 哈希表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import Counter     # 这里调用内置方法放方法内，这样使用时能直接调用
        return Counter(s) == Counter(t)

"""
    哈希表一般比排序快2-5倍（取决于数据量，数据量越大差距越明显）
    哈希表操作是O(1)的，而排序是O(nlogn)
    哈希表只需要遍历每个字符串一次O(n)，使用哈希表存储字符计数比较两个Counter对象也是O(n)，所以时间复杂度是O(2n)即O(n)
    排序需要对两个字符串进行排序，排序的时间复杂度是O(nlogn)，然后比较两个排序后的列表，需要O(n)，所以时间复杂度是O(nlogn+n)即O(n)
"""

# 字典
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for char in s:      # 记录字符串s每个字符（键）出现的次数（值）
            count[char] = count.get(char, 0) + 1    # 字典get(char, 0)表示取字典char键的值，如果为空则为char键赋值为0

        for char in t:      # 从字典中减去字符串t中每个字符（键）出现的次数（值）
            count[char] = count.get(char, 0) - 1    #
            if count[char] < 0:     # 当字典的字符（键）对应的次数（值）变为负时（字符串t有而字符串s没有）则返回False
                return False

        return True