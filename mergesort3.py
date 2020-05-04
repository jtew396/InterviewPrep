# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, left, middle, right):
	n1 = middle - left + 1
	n2 = right - middle

	# create temp arrays
	LeftArr = [0] * (n1)
	RightArr = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0 , n1):
		Left[i] = arr[left + i]

	for j in range(0 , n2):
		Right[j] = arr[middle + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2 :
		if Left[i] <= Right[j]:
			arr[k] = Left[i]
			i += 1
		else:
			arr[k] = Right[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = Left[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = Right[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,left,right):
	if left < right:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		middle = (left + (right - 1)) // 2

		# Sort first and second halves
		mergeSort(arr, left, middle)
		mergeSort(arr, middle + 1, right)
		merge(arr, left, middle, right)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
	print ("%d" %arr[i]),

mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
	print ("%d" %arr[i]),

# This code is contributed by Mohit Kumra
