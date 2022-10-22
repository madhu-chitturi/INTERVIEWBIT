link : https://www.interviewbit.com/problems/length-of-last-word/
    
     
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        a=A.split()
        b=list(a)
        if(len(b)>=1):
            c=len(b)
            if(b==1):
                return c
            else:
                d=b[c-1]
                e=list(d)
                f=len(e)
                return f
        else:
            return 0
