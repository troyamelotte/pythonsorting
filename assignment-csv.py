import csv
with open ('us-500.csv', 'rU') as f:
	reader = csv.reader(f)
	result = []
	for row in reader:
	    result.append(row)
for a in result:
	print a[0],a[1]
	for i in range(0,len(a)):

		print result[0][i], ':', a[i]
	print '------------------'
# here we loop through all the lists taking the first and last names in the print a[0]a[1] lines
#next we loop through each nested list where we print the first lists headers (firstname ect) by incrementing by one then we print the
#items in the lists with a[i]