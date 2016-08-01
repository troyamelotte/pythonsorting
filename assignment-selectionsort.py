
def selectionsort(arr):

	for i in range(0, len(arr)):
		currentnum=arr[i]
		min = i
		for num in range(i, len(arr)):
			if arr[num] < currentnum:
				currentnum = arr[num]	
				min=num			
		arr[min]=arr[i]
		arr[i]=currentnum	
from random import randint
a = [5,4,1,7,8,6,4,6,8,5,2,7,8578,65]
selectionsort(a)
print a