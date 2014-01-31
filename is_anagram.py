def isAnagram(str1,str2):
	if len(str1) != len(str2):
		return False
	arr = [0] * 256
	for i in str1:
		arr[ord(i)] += 1
	for i in str2:
		arr[ord(i)] -= 1
		if arr[ord(i)] < 0:
			return False
	return True

print isAnagram('abcd','dcab')
print isAnagram('abcd','adcab')
print isAnagram('abcd','acab')
