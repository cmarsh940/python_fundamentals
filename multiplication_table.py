#If you need user to input range use
# row = int(raw_input("Enter the first row number: "   ))
# col = int(raw_input("Enter the frist column number: "))

# inputs starting at 1-12
row = int(1)
col = int(1)

lastR = row + 12 # Creates 12 rows
firstC = col
lastC = col + 12 # Creates 12 columns


#while loop for col * row
while (row < lastR):
    while(col < lastC):
        print "%4d" % (col * row),
        col += 1

    col = firstC
    row += 1
    print
