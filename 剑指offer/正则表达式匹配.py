def match(s, pattern):
	if s is None or pattern is None:
		return False
	return matchCore(s,pattern)

def matchCore(s, pattern):
	if len(s)==0 and len(pattern)==0:
		return True
	if len(s)>0 and len(pattern)==0:
		return False
	if len(pattern)>1 and pattern[1]=='*':
		if len(s)>0 and (pattern[0]==s[0] or pattern[0]=='.'):
			# 如果第一个字符能匹配，有两种可能，一种可能是后面的也与字符串相等，一种是不相等
			return matchCore(s[1:],pattern) or matchCore(s,pattern[2:]) or matchCore(s[1:],pattern[2:])
		else:
			return matchCore(s,pattern[2:])
	else:
		if len(s)>0 and (pattern[0]==s[0] or pattern[0]=='.'):
			return matchCore(s[1:],pattern[1:])
		else:
			return False

if __name__ == '__main__':
 	 print(match('aa','a.'))