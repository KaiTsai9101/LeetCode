"""
    给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。



    示例 1：


    输入：head = [1,2,3,4]
    输出：[2,1,4,3]
    示例 2：

    输入：head = []
    输出：[]
    示例 3：

    输入：head = [1]
    输出：[1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归求解
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件
        if not head or not head.next:
            return head
        # 定义head的下一个节点
        newHead = head.next
        # 递归调用（将头节点索引指向下下个节点）
        head.next = self.swapPairs(newHead.next)
        # 将头节点的下一个节点的索引指向头节点
        newHead.next = head
        return newHead

# 迭代求解
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建临时头节点，指向下一个元素
        dummyHead = ListNode(0)
        dummyHead.next = head
        tmp = dummyHead

        # 当临时节点之后还有两个元素时才执行（两两交换需要两个元素）
        while tmp.next and tmp.next.next:
            node1 = tmp.next        # 初始设置node1为临时节点下一个元素
            node2 = tmp.next.next       # 初始设置node2为临时节点下下一个元素
            tmp.next = node2        # 将临时节点的下一个节点索引指向node2
            node1.next = node2.next     # 将node1节点的下一个节点索引指向node2节点的下一个节点
            node2.next = node1      # 将node2节点的下一个节点索引指向node1
            tmp = node1         # 将node1的值赋给tmp为下一组判断做准备
        return dummyHead.next