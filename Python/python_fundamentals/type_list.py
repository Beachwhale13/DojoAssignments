my_list = ["magical unicorn", 19, 'hello', 98.98, 'world']
#iterate through
sum = 0.0
string = ''
type = []

for item in my_list:
    if isinstance(item, int):
        sum += item
        type.append(0)
    elif isinstance(item,float):
        sum += item
        type.append(0)
    elif isinstance(item,str):
        string += " " + item
        type.append(1)
if 0 not in type:
    print "The list you entered is of string type"
elif 1 not in type:
    print "The list you entered is of integer type"
else:
    print "The list you entered is of mixed type"

print "sum:",  sum
print "string:",  string
