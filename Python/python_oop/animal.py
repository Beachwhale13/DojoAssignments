class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "The {}'s health is at level {}".format(self.name, self.health)


class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health -= 5
        return self

class Dragon(Animal):
    def __init__(self,name, health = 170):
        super(Dragon, self).__init__(name,health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon,self).display_health()
        print "I am a Dragon!!!"



lion = Animal("lion",200)
lion.walk().walk().walk().run().display_health()
doggo = Dog("dog")
doggo.walk().walk().walk().run().run().pet().display_health()
drogo = Dragon("drogo")
drogo.run().run().walk().fly().display_health()
girrie = Animal("giraffe", 100)
girrie.run().run().walk().display_health()
