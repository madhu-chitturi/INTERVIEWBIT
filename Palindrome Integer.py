link:  https://www.interviewbit.com/problems/palindrome-integer/
    
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A>=0:
            a=list(map(int,str(A)))
            b=a[::-1]
            if b==a:
                return 1
            else:
                return 0
        else:
            return 0
       
