link : https://www.interviewbit.com/problems/string-and-its-frequency/
    
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        str1=list(A)
        str2=[]
        for i in range(len(str1)):
            if str1[i] not in str2:
                str2.append(str1[i])
        dict1={}
        for i in range(len(str1)):
            if str1[i] not in dict1:
                dict1[str1[i]]=1
            else:
                dict1[str1[i]]+=1
        c=[]
        for i in range(len(str2)):
            c.append(str2[i])
            c.append(dict1[str2[i]])
        s=c[0]
        for i in range(1,len(c)):
            f=str(c[i])
            s+=f
        return s
        
