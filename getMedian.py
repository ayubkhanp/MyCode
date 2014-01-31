"""
def getMedian(arr1, arr2):
	i = j = k = 0
	count = 0
	m = len(arr1)
	n = len(arr2)
	arr3 =[]
	while(i < m and j < n ):#and i+j <= (m+n)/2):
		if arr1[i] < arr2[j]:
			arr3.append(arr1[i])
			i = i+1
		elif arr1[i] > arr2[j]:
			arr3.append(arr2[j])
                        j = j+1
		else:
			arr3.append(arr1[i])
			i = i+1
                        arr3.append(arr2[j])
                        j = j+1
	while(i < m):
		arr3.append(arr1[i])
		i = i+1
	while(j < n):
		arr3.append(arr2[j])
		j = j+1
	k = (m+n)/2
	if (m+n)%2 == 0:
		median = (arr3[k] + arr3[k-1])/2 
	else:
		median = arr3[k]
	print arr3
	print median
"""
def getMedian(arr1, arr2):
        i = j = k = 0
        count = 0
        m = len(arr1)
        n = len(arr2)

	k = (m+n)/2+1
	prev = cur = 0
	while( i < m and j < n and i+j < k ):
		prev = cur
		if arr1[i] < arr2[j]:
			cur =  arr1[i]
			i += 1
		elif arr1[i] > arr2[j]:
			cur =  arr2[j]
			j += 1
		else:
			cur = arr1[i]
			prev = arr2[j]
			i += 1
			j += 1
	
	#print cur, prev	
	if (m+n)%2 == 0:
		median = (cur+prev)/2
	else:
		median = cur
	print median

getMedian([ 1, 12, 14, 17, 26, 38],[2, 13, 16, 18, 30, 45])
