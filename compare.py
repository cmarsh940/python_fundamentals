list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]


list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]

list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

def compare(lst1, lst2):
    if len(lst1) != len(lst2):
        print "The lists are not the same"
    else:
        for index in range(len(lst1)):
            if lst1[index] == lst2[index] and (index == len(lst1)-1):
                print lst1[index], lst2[index]
                print "The lists are identical"
            elif lst1[index] == lst2[index]:
                print lst1[index], lst2[index]
                continue
            else:
                print lst1[index], lst2[index]
                print "The lists are not the same."
                break



print compare(list_one, list_two)

print compare(list_three, list_four)

print compare(list_five, list_six)

print compare(list_seven, list_eight)
