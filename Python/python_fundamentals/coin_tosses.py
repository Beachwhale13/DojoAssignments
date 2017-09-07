import random

def coin_toss():
    count = 1
    tail = 0
    head = 0
    print "Starting the program..."
    while (count <= 10):
        string = 'Attempt #{}: Throwing a coin...'.format(count)
        number = round(random.random())
        if (number == 0):
            string += " It's a head! ..."
            head += 1
        else:
            string += " It's a tail! ..."
            tail += 1
        count = count + 1
        string += " Got {} head(s) so far and {} tail(s) so far".format(head, tail)
        print string
    print "Ending the program, thank you!"
coin_toss()
