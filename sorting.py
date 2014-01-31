def sorting(arr):
	leastIndex = 0
	pivot = 0
	for i in range(0,len(arr)):
		if arr[i] < arr[pivot]:
			leastIndex = i
		 
		
