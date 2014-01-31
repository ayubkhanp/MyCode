def arrange(A,p):
	j = len(A)-1
	i = 0
	pivot = A[p]
	count =0 
	while(i != j):
		while (A[i] < pivot): 
			count += 1
			i += 1
		while (A[j] > pivot): 
			count += 1
			j -= 1
		temp = A[i]
		A[i] = A[j]
		A[j] = temp
	print A
	print count

arrange([25,5,8,12,6,2],4)
arrange([65,70,75,60,85,60,55,50,45],0)

