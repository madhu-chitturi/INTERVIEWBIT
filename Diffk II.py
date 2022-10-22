link : https://www.interviewbit.com/problems/diffk-ii/
    
    
  class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        dict1={}
        if(B==0):
            c=set(A)
            if(len(c)!=len(A)):
                return 1
            else:
                return 0
        for i in range(len(A)):
            if A[i] in dict1:
                dict1[A[i]]+=1
            else:
                dict1[A[i]]=1
        for i in range(len(A)):
            a=A[i]
            b=a-B 
            if b in dict1:
                c=1
                break
            else:
                c=0
        if(c==1):
            return 1
        else:
            return 0
                
