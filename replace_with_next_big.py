import sys

def replaceWithNextBig(arr):
	print arr
	length = len(arr)
	stack = []
	for i in xrange(length-1, -1, -1):
		if not len(stack):
			stack.append(arr[i])
			arr[i] = sys.maxint
		else:
			while len(stack) and arr[i] >= stack[-1]:
				stack.pop()
			if not len(stack):
				stack.append(arr[i])
				arr[i] = sys.maxint
			else:
				temp =  stack[-1]
				stack.append(arr[i])
				arr[i] = temp
	print arr

replaceWithNextBig([4,3,2,1,2,3,4])
replaceWithNextBig([25,6,-1,20,11,25,40,1])
