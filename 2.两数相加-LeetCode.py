"""
    给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

    请你将两个数相加，并以相同形式返回一个表示和的链表。

    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。



    示例 1：


    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
    示例 2：

    输入：l1 = [0], l2 = [0]
    输出：[0]
    示例 3：

    输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    输出：[8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val + l2.val >= 10:  # 判断进位
            i = 1
        else:
            i = 0
        node1 = ListNode((l1.val + l2.val) % 10)  # 保留头节点node1
        node = node1  # 创建临时节点node
        """
            # 第1步：创建头节点
            node1 = ListNode(7)    # node1 → [7|•]
            node = node1          # node 也指向 [7|•]

            # 现在：node1 → [7|None]
            #       node → [7|None]

            # 第2步：添加第二个节点
            node.next = ListNode(0)  # node1 → [7|→] → [0|None]
                                    # node → [7|→] → [0|None]
            node = node.next        # node1 → [7|→] → [0|None]
                                    # node → [0|None]

            # 第3步：添加第三个节点  
            node.next = ListNode(8)  # node1 → [7|→] → [0|→] → [8|None]
                                    # node → [0|→] → [8|None]
            node = node.next        # node1 → [7|→] → [0|→] → [8|None]
                                    # node → [8|None]

            # 最终：
            # node1 指向第一个节点 7（头节点）
            # node 指向最后一个节点 8
        """

        # 当l1和l2都还有数时
        while l1.next and l2.next:
            node.next = ListNode((l1.next.val + l2.next.val + i) % 10)
            if l1.next.val + l2.next.val + i >= 10:  # 判断进位
                i = 1
            else:
                i = 0

            l1 = l1.next
            l2 = l2.next
            node = node.next

        # 当l1比l2长
        while l1.next:
            node.next = ListNode((l1.next.val + i) % 10)
            if l1.next.val + i >= 10:  # 判断进位
                i = 1
            else:
                i = 0

            l1 = l1.next
            node = node.next

        # 当l2比l1长
        while l2.next:
            node.next = ListNode((l2.next.val + i) % 10)
            if l2.next.val + i >= 10:  # 判断进位
                i = 1
            else:
                i = 0

            l2 = l2.next
            node = node.next

        """
            当最后没有数字时i还是为1则进1位
            例：999 + 1 = 1000
        """
        if i == 1:
            node.next = ListNode(1)

        return node1

# 本题主要考链表操作，需注意对每个参数引用（指针）的指向更新