LINK: https://www.interviewbit.com/problems/two-out-of-three/


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        a=set(A)
        x=list(a)
        b=set(B)
        y=list(b)
        c=set(C)
        z=list(c)
        dict1={}
        d=A+B+C 
        f=set(d)
        h=list(f)
        for i in range(len(x)):
            if x[i] not in dict1:
                dict1[x[i]]=1
            else:
                dict1[x[i]]+=1
        for i in range(len(y)):
            if y[i] not in dict1:
                dict1[y[i]]=1
            else:
                dict1[y[i]]+=1
        for i in range(len(z)):
            if z[i] not in dict1:
                dict1[z[i]]=1
            else:
                dict1[z[i]]+=1
        s=[]
        for i in range(len(h)):
            if(dict1[h[i]]>=2):
                s.append(h[i])
        t=sorted(s)
        return t
