def merge(A,B):
	i = j = 0
	C = []
	while(i < len(A) and j < len(B)):
		if (A[i] <= B[j]) : 
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
	while(i < len(A)):
		C.append(A[i])
		i +=1
	while(j < len(B)):
		C.append(B[j])
		j += 1
	
	print C

merge([1,7,21,36],[2,9,15,42])

