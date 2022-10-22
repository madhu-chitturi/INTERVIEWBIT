link: https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
    
    
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
        n=len(A)
        m=len(B)
        for t in range(m):
            A.append(0)
        c=[0 for x in range(n+m)]
        i=0
        j=0
        k=0
        while(i<n and j<m):
            if(A[i]<B[j]):
                c[k]=A[i]
                k+=1
                i+=1
            else:
                c[k]=B[j]
                k+=1
                j+=1
        while(j<m):
            c[k]=B[j]
            k+=1
            j+=1
        while(i<n):
            c[k]=A[i]
            k+=1
            i+=1
        for i in range(0,n+m):
            A[i]=c[i]
