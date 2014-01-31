count = 0
def perm(arr, start, end):
	if start == end:
		global count
		count = count+1
		print arr
	else:
		for i in range(start, end):
			t = arr[start]
			arr[start] = arr[i]
			arr[i] = t
			perm(arr, start+1, end)
#			t = arr[start]
#			arr[start] = arr[i]
#			arr[i] = t
	

perm(range(0,10),0,10) 
#perm(range(0,5),0,5) 
print count
