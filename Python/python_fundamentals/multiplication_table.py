x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [1,2,3,4,5,6,7,8,9,10,11,12]

z = 0
while (z < len(y)):
    for num in x:
        print (y[z]*num),
    z = z + 1
    print '\n'
