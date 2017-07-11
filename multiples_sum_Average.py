#Multiples
#part 1
for x in range(1,1000):
	if x % 3 == 0:
		print x

# #part 2
for y in range(5,1000005):
	if y % 5 == 0:
		print y

#sum list
a = [1,2,5,10,255,3]
def sum(lst):
	total = 0
	for num in lst:
		total += num
	print total
sum(a)

#Average List
a = [1,2,5,10,255,3]
def avg(lst):
    total = 0.0
    count = 0
    for num in lst:
        total += num
        count += 1
    print total/count	
avg(a)