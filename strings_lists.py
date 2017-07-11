words = "it's thanksgiving day. It's my birthday,too!"
first_day = words.find('day')
print first_day #
new =words.replace('day', 'month')
print new #"it's thanksgiving month. It's my birthday,too"

#Min/Max
x = [2,54,-2,7,12,98] #-2,98
print min(x)
print max(x)


#First/Last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0], x[7] # "hello" "world"
new_x = [x[0], x[-1]]
print new_x

#New List
num = [19,2,54,-2,7,12,98,32,10,-3,6]
num.sort() #[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
halfway = len(num)/2
start = num[:halfway]
end = num[halfway:]

new_list = [start]
New_list2 = [start]
print new_list #[[-3,-2,2,6,7]]
for number in end:
    new_list.append(number)
print new_list #[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]
