class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def preorder(A,li):
        if A==None:
            return
        li.append(A.val)
        Solution.preorder(A.left,li)
        Solution.preorder(A.right,li)
	def preorderTraversal(self, A):
        li=[]
        Solution.preorder(A,li)
        return li
