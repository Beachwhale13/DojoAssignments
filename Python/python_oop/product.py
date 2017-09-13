class Product(object):
    def __init__(self, item_name, weight, brand, cost):
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.price = self.tax()
        self.status = "for sale"
        self.display_info()

    def tax(self):
        self.price = self.cost*1.08
        return self.price

    def sell(self):
        self.status = "sold"
        return self

    def return_item(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box like new":
            self.status = "for sale"
        elif reason == "open box":
            self.status = "used"
            self.price = self.price - (self.price*.20)
        return self

    def display_info(self):
        print "Item Name:", self.item_name
        print "Cost:", self.cost
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self


item1 = Product("Boba", ".13lb", "drink", 3)
item1.return_item("defective").display_info()
item1.sell().display_info()
