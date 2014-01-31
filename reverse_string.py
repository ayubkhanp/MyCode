def myReverse(string):
	start = 0
	end = len(string)-1
	while start < end:
		tmp = string[start]
		string[start] = string[end]
		string[end] = tmp
		start += 1
		end -= 1
	print string
	return string

print myReverse('ayub')
