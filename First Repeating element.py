link:  https://www.interviewbit.com/problems/first-repeating-element/
  
    class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        dict1={}
        d=0
        for i in range(len(A)):
            if A[i] in dict1:
                dict1[A[i]]+=1
                
            else:
                dict1[A[i]]=1
        for j in range(len(dict1)):
            if(dict1[A[j]]>=2):
                    c=A[j]
                    d=1
                    break        
        if(d==0):
            return -1
        else:
            return c
