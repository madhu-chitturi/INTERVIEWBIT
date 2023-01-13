class Solution:
    def inorder(A,li):
        if(A==None):
            return
        Solution.inorder(A.left,li)
        li.append(A.val)
        Solution.inorder(A.right,li)
	def inorderTraversal(self, A):
        li=[]
        Solution.inorder(A,li)
        return li
