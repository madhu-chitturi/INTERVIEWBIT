class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorder(A,li):
		if A==None:
			return
		Solution.postorder(A.left,li)
		Solution.postorder(A.right,li)
		li.append(A.val)
	def postorderTraversal(self, A):
		li=[]
		Solution.postorder(A,li)
		return li
