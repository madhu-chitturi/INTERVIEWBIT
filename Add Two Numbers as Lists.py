class Solution:
	def addTwoNumbers(self, A, B):
        nn=ListNode(-1)
        tmp=nn
        c=0
        while(A!=None and B!=None):
            a=A.val+B.val+c
            b=a%10
            n=ListNode(b)
            nn.next=n
            nn=nn.next
            c=a//10
            A=A.next
            B=B.next
        while(A!=None):
            a=A.val+c
            b=a%10
            n=ListNode(b)
            nn.next=n
            nn=nn.next
            c=a//10
            A=A.next
        while(B!=None):
            a=B.val+c
            b=a%10
            n=ListNode(b)
            nn.next=n
            nn=nn.next
            c=a//10
            B=B.next
        if(c==1):
            n=ListNode(1)
            nn.next=n
        return tmp.next
        
