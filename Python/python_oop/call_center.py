import itertools

class Call(object):
    id_generator = itertools.count(1)
    def __init__(self, name, phone_number, time, reason):
        self.id = next(self.id_generator)
        self.name = name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason
        # self.display()

    def display(self):
        print "ID: {}. Caller: {} Phone number: {} Time: {} Reason: {}".format(self.id, self.name, self.phone_number, self.time, self.reason)


call1 = Call("Sandy", "(123)123-1234", "11:34", "Just because")
call2 = Call("Kai", "(321)321-4321", "11:45", "Cause I'm your Bro")
call3 = Call("Yao", "(345)345-1234", "12:00", "I need to play Pokemon")


class Callcenter(object):
    def __init__(self):
        self.list_of_calls = []
        self.queue_size = 0

    def add(self, call):
        self.list_of_calls.append(call)
        self.queue_size = len(self.list_of_calls)
        return self

    def remove(self):
        self.list_of_calls.pop(0)
        return self

    def display_list(self):
        for call in self.list_of_calls:
            print call.name, call.phone_number
        return self

    def find_and_remove(self, number):
        for call in self.list_of_calls:
            if call.phone_number === number:
                self.list_of_calls.pop(call)

    def sort_by_time(self):
        self.list_of_calls.sort(call.time)



myCallcenter = Callcenter()
myCallcenter.add(call1).add(call2).add(call3).display_list()
myCallcenter.remove().display_list()
