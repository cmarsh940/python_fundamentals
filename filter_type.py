#integer
def integer(num):
	if isinstance(num, int):
		if num < 100:
			print "That's a small number"
		else:
			print "That's a big number"
integer(500)

#String
def string(new):
	if isinstance(new, str):
		if len(new) < 50:
			print "Short sentence"
		else:
			print "Long sentence"
string("hello")

#List
def list_(lst):
	if isinstance(lst, list):
		if len(lst) < 10:
			print "Short list"
		else:
			print "Long list"

aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ["name","address","phone number","social security number"]

list_(aL)
list_(mL)
list_(lL)
list_(eL)
list_(spL)