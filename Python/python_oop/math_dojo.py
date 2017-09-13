class MathDojo(object):
    def __init__(self):
        self.num = 0

    def add(self, *args):
        for entry in args:
            if type(entry) == int:
                self.num += entry

            else:
                for i in range(len(entry)):
                    self.num += entry[i]
        return self

    def subtract(self, *args):
        for entry in args:
            if type(entry) == int:
                self.num -= entry

            else:
                for i in range(len(entry)):
                    self.num += entry[i]
        return self

    def result(self):
        print self.num

md = MathDojo()
# md.add(2).add(2,5).subtract(3,2).result()
# md.add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
