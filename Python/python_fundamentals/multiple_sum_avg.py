#print odd numbers from 1 to 1000
for i in range(1, 1001, 2):
    print i

#print multiples of 5 from 5 to 1,000,000
for i in range(5, 1000001, 5):
    print i

#sumlist - prints the sum of all values in list
a = [1,2,5,10,255,3]
print sum(a)

#averagelist - average of list
average = sum(a)/len(a)
print average
