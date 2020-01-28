def isTrue(s:str)->bool:
	if str is None:
		return False
	hasdot = False
	hassign = False
	hase = False
	for i in range(len(s)):
		if s[i]=='.':                  # . 出现的地方只能是e没出现，并且. 也没出现过地方
			if hasdot or hase or i==len(s)-1:
				return False
			hasdot = True
		elif s[i]=='e' or s[i]=='E':   # E出现后，说明不能再出现E，并且E不能是最后一个
			if hase or i==len(s)-1:
				return False
			hase = True
		elif s[i]=='+' or s[i]=='-':   # 符号可能出现的地方，整数部分的第一个，E部分的第一个
			if hassign and s[i-1]!='e' and s[i-1]!='E':
				return False
			if not hassign:
				if i!=0 and s[i-1]!='e' and s[i-1]!='E':
					return False
			hassign = True
		else:
			if s[i]<'0' or s[i]>'9':
				return False
	return True

print(isTrue('.e'))