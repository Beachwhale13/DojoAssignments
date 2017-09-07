words = "It's thanksgiving day. It's my birthday, too!"

#print position of the first instance of the word "day"
print words.find("day")

#new string where "day" is replaced with "month"

print words.replace("day", "month")

#min and max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#first and last
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[-1]
new_list = [x[0], x[-1]]
print new_list

#newlist - sort
z = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
z.sort()
print z

#newlist - half of the list into a new array
new_list =  z[0:len(z)/2]
z = z[len(z)/2:len(z)]
print z
print new_list

#insert into position 0
z.insert(0, new_list)
print z
