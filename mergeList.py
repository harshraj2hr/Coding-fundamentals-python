class ListNode(object):
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next



def merge( list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy=ListNode(0)
        cur=dummy
        p=list1
        q=list2
        while p and q:
            if p.val<=q.val:
                cur.next=p
                p=p.next
            else:
                cur.next=q
                q=q.next
            cur=cur.next
        if p:
            cur.next=p
        else:
            cur.next=q
        
        return dummy.next

a=ListNode(5)
a.next=ListNode(6)
a.next.next=ListNode(9)
a.next.next.next=ListNode(9)

b=ListNode(2)
b.next=ListNode(5)

a=merge(a,b)
temp=a
while temp:
   print(temp.val)
   temp=temp.next
