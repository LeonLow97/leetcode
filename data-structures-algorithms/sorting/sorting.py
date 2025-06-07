# Merge Sort
def merge_sort(nums):
	if nums is None or len(nums) == 0: return []
	if len(nums) == 1: return nums

	# Divide
	midpoint = len(nums) // 2
	left_arr = nums[:midpoint]
	right_arr = nums[midpoint:]

	# Conquer
	merge_sort(left_arr)
	merge_sort(right_arr)

	l = r = i = 0
	while l < len(left_arr) and r < len(right_arr):
		if left_arr[l] < right_arr[r]:
			nums[i] = left_arr[l]
			l += 1
		else:
			nums[i] = right_arr[r]
			r += 1
		i += 1

	while l < len(left_arr):
		nums[i] = left_arr[l]
		l += 1
		i += 1
	while r < len(right_arr):
		nums[i] = right_arr[r]
		r += 1
		i += 1
	
	return nums

# Insertion Sort
def insertion_sort(nums):
	if nums is None or len(nums) == 0: return []
	if len(nums) == 1: return nums

	for i in range(1, len(nums)):
		j = i
		while j > 0 and nums[j] < nums[j-1]:
			nums[j], nums[j-1] = nums[j-1], nums[j]
			j -= 1
		
	return nums

# Quick Sort
def quick_sort(nums):
	if nums is None or len(nums) == 0: return []
	if len(nums) == 1: return nums

	left, right = 0, len(nums) - 1
	def _quick_sort(nums, left, right):
		# condition holds true means we need to partition array
		if left < right:
			partition_pos = partition(nums, left, right)
			_quick_sort(nums, left, partition_pos - 1)
			_quick_sort(nums, partition_pos + 1, right)
		return nums
	
	return _quick_sort(nums, left, right)

def partition(nums, left, right):
	pivot = nums[right]
	l = left
	for r in range(left, right):
		# bring all smaller numbers than pivot to left side of array
		if nums[r] < pivot:
			nums[l], nums[r] = nums[r], nums[l]
			l += 1
	
	# move pivot to left position (last pos that has element >= pivot)
	nums[l], nums[right] = nums[right], nums[l]
	return l

# Selection Sort
def selection_sort(nums):
	if nums is None or len(nums) == 0: return []
	if len(nums) == 1: return nums

	for i in range(1, len(nums)):
		cur_min_idx = i
		for j in range(i+1, len(nums)):
			if nums[j] < nums[cur_min_idx]:
				cur_min_idx = j
		nums[i], nums[cur_min_idx] = nums[cur_min_idx], nums[i]
	
	return nums

def tests(fns):
	test_cases = [
		{
			"title": "all positive numbers",
			"input": [4, 3, 0, 9, 6, 1, 2],
			"expected": [0, 1, 2, 3, 4, 6, 9],
		},
		{
			"title": "all positive numbers with duplicates",
			"input": [1, 2, 2, 1, 1, 0, 0, 2, 2, 1, 0, 0, 3, 2],
			"expected": [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3],
		},
		{
			"title": "all negative numbers",
			"input": [-5, -1, -3, -2, -4],
			"expected": [-5, -4, -3, -2, -1],
		},
		{
			"title": "mix of positive and negative",
			"input": [3, -2, -1, 0, 2, -3, 1],
			"expected": [-3, -2, -1, 0, 1, 2, 3],
		},
		{
			"title": "already sorted array",
			"input": [1, 2, 3, 4, 5],
			"expected": [1, 2, 3, 4, 5],
		},
		{
			"title": "reverse sorted array",
			"input": [5, 4, 3, 2, 1],
			"expected": [1, 2, 3, 4, 5],
		},
		{
			"title": "array with all same elements",
			"input": [1, 1, 1, 1, 1],
			"expected": [1, 1, 1, 1, 1],
		},
		{
			"title": "empty array",
			"input": [],
			"expected": [],
		},
		{
			"title": "single element array",
			"input": [42],
			"expected": [42],
		},
		{
			"title": "large numbers",
			"input": [100000, 99999, 1234567, -1234567],
			"expected": [-1234567, 99999, 100000, 1234567],
		},
	]

	all_tests_pass = True
	for function_name, func in fns:
		print("\t***** Running", function_name, "*****")
		for test in test_cases:
			actual = func(test["input"])
			if actual != test["expected"]:
				print("FAIL:", test["title"])
				all_tests_pass = False
			else:
				print("PASS:", test["title"])
		
	return all_tests_pass

functions = [
	["Merge Sort", merge_sort],
	["Insertion Sort", insertion_sort],
	["Quick Sort", quick_sort],
	["Selection Sort", selection_sort]
]

if tests(functions):
	print("✅ All tests passed!")
else:
	print("❌ Some test(s) failed!")
