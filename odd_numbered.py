def find_odd_occurence(arr):
	myhash = {}
	for i in arr:
		if i in myhash:
			del myhash[i]
		else: myhash[i] = 1
	print myhash.keys()

find_odd_occurence([1,2,2,2,1,3,3,3,3,4,4,4,4,4,5,6,6,7,7,])
