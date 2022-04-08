'''
定义两个指针，一快一慢。慢指针每次只移动一步，而快指针每次移动两步。
初始时，慢指针在位置 head,而快指针在位置 head.next。
如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。
否则快指针将到达链表尾部，该链表不为环形链表。
例题：leetcode 141环形链表
'''
# 判断是否有回路

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


def hasCycle(self, head:ListNode) -> bool:
        if not head:
            return False
        l1 = head
        l2 = head.next
        while l1 and l2 and l2.next:
            if l1 == l2:return True
            l1 = l1.next
            l2 = l2.next.next
        return False
