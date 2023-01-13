class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        l=[]
        while(A!=None):
            l.append(A.val)
            A=A.next
        li=sorted(l)
        n=ListNode(-1)
        tmp=n 
        for i in range(len(li)):
            nn=ListNode(li[i])
            n.next=nn
            n=n.next
        return tmp.next
