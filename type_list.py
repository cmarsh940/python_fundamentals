
l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

def list_(lst):
    new_string = ''
    total = 0
    for item in lst:
        if isinstance(item, int) or isinstance(item, float):
            total += item
        elif isinstance(item, str):
            new_string += item

    if new_string and total:
        print 'The array you entered is of mixed type'
        print 'String:', new_string
        print 'Total:', total
    elif new_string:
        print 'The array you entered is of string type'
        print 'String:',new_string
    else:
        print 'The array you entered is of number(float or int) type'
        print 'Total:', total

print
list_(l1)
print
list_(l2)
print
list_(l3)



# #input
#l1 = ['magical unicorns',19,'hello',98.98,'world']

# #output
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"


# # input
# l2 = [2,3,1,7,4,12]

# #output
# "The array you entered is of integer type"
# "Sum: 29"


# # input
# l3 = ['magical','unicorns']

# #output
# "The array you entered is of string type"
# "String: magical unicorns"