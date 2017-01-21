def reverseWords(s):
	t = [word for word in s.strip().split() if word != ' ']
	t.reverse()
	print(type(t))
	print(t)
	return ' '.join(t)

def main():
	s = "   a   b "
	print(reverseWords(s))
	b()

def b():
	print('b')

if __name__ == '__main__':
	main()