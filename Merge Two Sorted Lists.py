class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        prev=ListNode(-1)
        tmp=prev
        while(A!=None and B!=None):
            if(A.val<B.val):
                prev.next=A
                A=A.next
            else:
                prev.next=B
                B=B.next
            prev=prev.next
        if(A!=None):
            prev.next=A
        else:
            prev.next=B
        return tmp.next
