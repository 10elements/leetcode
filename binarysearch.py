__author__ == 'Dimitri Zhang'

def binarysearch(nums, target):
	l = len(nums)
	i, j = 0, l - 1
	while i <= j:
		mid = (i + j) >> 1
		if nums[mid] < target:
			i = mid + 1
		elif nums[mid] > target:
			j = mid - 1
		else:
			i = mid
			break
	return i
