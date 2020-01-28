def replaceBlackpy(s:str)->str:
	s = list(s)

	def replace(char):
		if char == ' ':
			return '%20'
		else:
			return char

	s = list(map(replace,s))
	s = ''.join(s)
	return s

def replaceBlack(s:str)->str:
	blackNum = 0
	for i in s:
		if i == ' ':
			blackNum += 1
	first = len(s)-1
	second = len(s)+2*blackNum-1
	s = s+' '*blackNum*2
	s = list(s)
	while first>=0 and first<second :
		if s[first]==' ':
			s[second] = '0'; second -= 1;
			s[second] = '2'; second -= 1;
			s[second] = '%'; second -= 1;
		else:
			s[second] = s[first]; second -= 1;
		first -= 1
	return ''.join(s)


			
s = "    We are     happy "
print(replaceBlackpy(s))
print(replaceBlack(s))