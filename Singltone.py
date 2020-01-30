# class Singleton:
#    existence = None

#    def __new__(cls):
#        if cls.existence is None:
#            cls.existence = super(Singleton, cls).__new__(cls)
#        return cls.existence


# def SingletonDecorator(cls):
#    cash = {}
#
#    def wrapper(*args, **kwargs):
#        if cls not in cash:
#           cash[cls] = cls(*args, **kwargs)
#        return cash[cls]

#    return wrapper


def SingletonDecorator(self):
    cash = {}

    def wrapper(*args, **kwargs):
        if self not in cash:
            cash[self] = self
        return cash[self]

    return wrapper


@SingletonDecorator
class Foo: pass


if __name__ == '__main__':
    #s = Singleton()
    #print(s)
    #s1 = Singleton()
    #print(s1)
    a = Foo()
    b = Foo()
    print(a is b)
