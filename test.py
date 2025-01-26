class Person:
    def __init__(self, name, old, num):
        self.__name = name
        self.__old = old
        self.num = num

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    def id(self):
        pass

    def new_meth(self, num):
        return num

    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)

p = Person('Artur', 20)
p.__dict__['old'] = 'old in obj p'
a = p.old
p.old = 10
print(p.old, p.__dict__)