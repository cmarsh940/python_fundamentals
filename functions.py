def fun():
	for x in range(1,2000):
		if x%2 == 0:
			print "Number is " + str(x) + ". This is an even number."
		else:
			print "Number is " + str(x) + ". This is an odd number."
fun()

def multiply(a, b=5):
	for l in range(len(lst)):
		a[l] *= b
	return lst

multiply[2,4,10,16]

def layered_multiples(arr):
    output = []
    for num in arr:
        temp_list = []
        count = 1
        while count <= num:
            temp_list.append(1)
            count += 1
        output.append(temp_list)
    return output
print layered_multiples([1,2,3])

a = [2,4,5]

print layered_multiples(multiply(a, 3))
