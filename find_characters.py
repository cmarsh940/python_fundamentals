def find_(lst, char):
    new_list = []
    for word in lst:
        if char in word:
            new_list.append(word)
    return new_list

list_ = ['hello','world','my','name','is','Anna']
char = 'o'

print find_(list_, char)