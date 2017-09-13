class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "This bike is", self.price,". It has a max_speed of", self.max_speed,". It is at", self.miles,"miles"

    def ride(self):
        print "Riding..."
        self.miles = self.miles + 10
        print "At", self.miles, "miles"
        return self


    def reverse(self):
        print "Reversing..."
        self.miles = self.miles - 5
        if (self.miles > 0):
            print "At", self.miles, "miles"
        else:
            self.miles = 0
            print "Can't reverse into black holes"
        return self


Bike1 = Bike("$50", "5mph")
Bike2 = Bike("$100", "15mph")
Bike3 = Bike("$500", "50mph")

Bike1.ride().ride().ride().reverse().displayInfo()
Bike2.ride().ride().reverse().reverse().displayInfo()
Bike3.reverse().reverse().reverse().displayInfo()
