def compress(s):
	if not len(s):
		return s
	i = 0
	res = []
	for j in range(len(s)):
		if s[j] != s[i]:
			res.append(s[i] + str(j - i))
			i = j
	res.append(s[i] + str(j - i + 1))
	return ''.join(res)

def main():
	s = 'ab'
	r = compress(s)
	print(r)

if __name__ == '__main__':
	main()