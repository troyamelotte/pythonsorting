listerino = []
import time
startTime = time.time()
swapped=False;
from random import randint

for num in range(0,101):
	listerino.append(randint(0,100))
def bublesort(arr):
	swapped=False;
	for i in range(0, len(arr)):
		if (i==len(arr)-1):
			print 'done'
		elif arr[i]>arr[i+1]:
			temp = arr[i]
			arr[i] = arr[i+1]
			arr[i+1] = temp
			swapped=True
	if swapped:
		bublesort(arr)
	return arr

bublesort(listerino)
print listerino
print "It took " + str(time.time() - startTime)