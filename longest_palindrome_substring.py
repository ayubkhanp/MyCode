def LPS(string):
	maxlength = 1
	start = 0
	low = high = 0
	for x in range(0, len(string)):
		#`palindromes of odd length
		low = x-1
		high = x
		while low >= 0 and high < len(string) and string[low] == string[high]:
			if high - low + 1 > maxlength:
				maxlength = high - low + 1
				start = low
			low -= 1
			high += 1
			print string[low+1:high]			

                #`palindromes of even length
                low = x-1
                high = x+1
                while low >= 0 and high < len(string) and string[low] == string[high]:
                        if high - low + 1 > maxlength:
                                maxlength = high - low + 1
                                start = low
                        low -= 1
                        high += 1
			print string[low+1:high]			


	print string[start:start+maxlength]

LPS('abfdRacecaRAbAorTITabcdef')
