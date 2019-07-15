"""
URL : https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "val : {}, next : {}".format(self.val, self.next.val)

def print_list(head):
    currnet = head

    while currnet:
        print str(currnet.val) + " ->",
        currnet = currnet.next

    print "Null"

class Solution():
    def oddEvenList(self, head):
        if not head:
            return head

        p, q = head, head
        while q:
            q = q.next
            if not q or not q.next:
                break
                
            next_p, next_q = p.next, q.next
            q.next = next_q.next
            p.next, next_q.next = next_q, next_p
            p = p.next
            #print_list(head)
        return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
s.oddEvenList(n1)
