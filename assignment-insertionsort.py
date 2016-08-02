
#def insertionsort(arr):
#	for i in range(0, len(arr)):
#		count = 0
#		for num in range(0, len(arr)):
#			if arr[i]> arr[num]:
#				count+=1
#		arr.insert(count,arr[i])
#		arr.pop(i)
#		print arr

def insertionsort(arr):
	for index in range(0, len(arr)):
		sub = arr[index]
		while index-1 >=0 and sub<arr[index-1]:
			arr[index] = arr[index-1]
			index-=1
			arr[index]=sub
a = [5,3,10,2,5,8,7,9,3,4]
insertionsort(a)
print a			