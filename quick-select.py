def quickSelect(arr, first, last, target):
	print 'original', arr
	pivot = target-1
	left = first
	right = last
	while left < right:
		while arr[left] < arr[pivot]:
			left += 1
		while arr[right] > arr[pivot]:
			right -= 1
		if left < right:
			tmp = arr[left]
			arr[left] = arr[right]
			arr[right] = tmp
		if left == pivot: left = first
		if right == pivot: right = last
		print arr
	print arr[left]

#quickSelect([2,-4,5,6,0,7,-1,10,9], 0 , 8, 8)
#quickSelect([2,-4,5,6,0,7,-1,10,9], 0 , 8, 9)
quickSelect([2,-4,5,6,0,7,-1,10,9], 0 , 8, 5)
#quickSelect([2,-4,5,6,0,7,-1,10,9], 0 ,8, 2)
#quickSelect([2,-4,5,6,0,7,-1,10,9], 0 , 8, 1)
