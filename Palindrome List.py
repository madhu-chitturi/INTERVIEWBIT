class Solution:
	def lPalin(self, A):
        a=[]
        while(A!=None):
            a.append(A.val)
            A=A.next
        b=a[::-1]
        if(a==b):
            return 1
        else:
            return 0
