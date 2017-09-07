value = "Experience is simply the name we give our mistakes"
#check what type the value is:

#check value to see if it's greater or less than 100
if isinstance(value, int):
    if value > 100:
        print "That's a big number"
    elif value < 100:
        print "That's a small number"
elif isinstance(value, str):
    if len(value) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"
elif isinstance(value, list):
    if len(value) >= 10:
        print "Big list!"
    else:
        print "Short list"
