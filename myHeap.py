__author__ = 'Dimitri Zhang'

class myHeap(object):
	"""
	a min-heap
	"""
	def __init__(self):

		# a list where elements rest, reresenting a binary tree
		self.heap = []

		# the size of heap
		self.size = 0

	def __str__(self):
		return str(self.heap)

	def __iter__(self):
		return iter(self.heap)

	def __getitem(self, key):
		try:
			return self.heap[key]
		except IndexError:
			raise
		except TypeError:
			raise 

	def insert(self, val):
		"""
		insert an element into the heap in O(logn) time, n is the number of elements in the heap
		"""

		# append the element to the end of heap
		self.heap.append(val)

		# increase heap size by 1
		self.size += 1

		# if more than 1 element in the heap, then swap nodes if necessary to mantain the heap property
		if self.size > 1:

			# the index of the newly-added element
			index = self.size - 1

			# the index of the newly-added element's parent
			parent = (index - 1) >> 1

			# while the current node is smaller than its parent, swap it with its parent
			while self.heap[parent] > self.heap[index]:
				tmp = self.heap[parent]
				self.heap[parent] = self.heap[index]
				self.heap[index] = tmp

				# set index to its parent
				index = parent

				# reach the root, the heap invariance is fully restored
				if index == 0:
					break
					
				# the parent of current index
				parent = (index - 1) >> 1

	def pop(self):
		"""
		pop the smallest element fromt the heap, mantain heap invariant
		"""
		if self.size == 0:
			return None
		top = self.heap[0]
		if self.size == 1:
			del self.heap[0]
			self.size -= 1
			return top
		self.heap[0] = self.heap[-1]
		del self.heap[-1]
		self.size -= 1
		index = 0
		left = index * 2 + 1
		right = index * 2 + 2
		smallest = index
		while True:
			if left < self.size and self.heap[left] < self.heap[smallest]:
				smallest = left
			if right < self.size and self.heap[right] < self.heap[smallest]:
				smallest = right
			if smallest != index:
				tmp = self.heap[index]
				self.heap[index] = self.heap[smallest]
				self.heap[smallest] = tmp
				index = smallest
				left = index * 2 + 1
				right = index * 2 + 2
			else:
				break
		return top

	def heapify(self, arr):
		"""
		heapify an arbitrary array into a min-heap in O(n) time in a bottom-up manner
		"""
		self.size = len(arr)
		index = self.size - 1

		# if arr is not empty, heapify arr
		if self.size:
			for i in range((index - 1) // 2, -1, -1):
				self.minHeapify(arr, i)
		self.heap = arr

	def minHeapify(self, arr, index):
		"""
		heapify the subtree rooted at index in list arr
		"""
		smallest = index
		left = index * 2 + 1
		right = index * 2 + 2
		length = len(arr)
		if left < length and arr[left] < arr[smallest]:
			smallest = left
		if right < length and arr[right] < arr[smallest]:
			smallest = right
		if smallest != index:
			tmp = arr[index]
			arr[index] = arr[smallest]
			arr[smallest] = tmp
			self.minHeapify(arr, smallest)

	def peek(self):
		"""
		retrieve but not pop the top element from the heap
		"""
		# if heap is not empty
		if self.size:
			return self.heap[0]

		# return None if the heap is empty
		return None

	def isEmpty(self):
		"""
		check if the heap is empty
		"""
		return self.size == 0

def main():
	heap = myHeap()
	# heap.insert(1)
	# heap.insert(3)
	# heap.insert(2)
	# heap.insert(0)
	# print(heap)
	# while not heap.isEmpty():
	# 	print(heap.pop())
	# print(heap.pop())
	heap.heapify([4,1,3,2,4,1])
	print(heap)
	while not heap.isEmpty():
		print(heap.pop())

if __name__ == '__main__':
	main()
