def compress(str1):
	arr = [0] * 256
	newstr = ''
	str2 = ''
	for i in str1:
		arr[ord(i)] += 1
		if arr[ord(i)] == 1:
			newstr = newstr+i

	if len(newstr)*2 >= len(str1):
		return str1
	for i in newstr:
		str2 = str2+i+str(arr[ord(i)])
	return str2

print compress('aaabbbaaacccbbbeeffgg')
print compress('aabbcceeffgg')
print compress('eeffggaaabbbaaacccbbbeeffgg')
