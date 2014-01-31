def isStringUnique(string):
	if len(string) > 256:
		return False
	array = [0]*256
	for i in range(0,len(string)):
		if array[ord(string[i])]:
			return False
		array[ord(string[i])] += 1
	return True


print isStringUnique('abcdefgh')
print isStringUnique('abcaefgh')
