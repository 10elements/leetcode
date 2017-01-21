class T(object):
	"""docstring for T"""
	v = 0# class variable v
	def __init__(self):
		super(T, self).__init__()
		print(self.v)# reference class variable via instance

	def c(self):
		T.v = 1
		
def main():
	t = T()
	print(T.v)
	print(t.v)
	t.c()
	print(T.v)
	print(T.__dict__)
	# print(t.__dict__)

if __name__ == '__main__':
	main()