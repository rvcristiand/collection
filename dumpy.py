class MyClass:
    pass

myObj = MyClass()
myObj.x = 1; myObj.y = 2; myObj.z = 3

print(myObj.__dict__)  # {'x': 1, 'y': 2, 'z': 3}

class MyClass:
    __slots__ = ['x', 'y', 'z']

myObj = MyClass()
myObj.x = 1; myObj.y = 2; myObj.z = 3

try:
    print(myObj.__dict__)
except Exception as e:
    print(e)  # 'MyClass' object has no attribute '__dict__'

try:
    myObj.w = 0
except Exception as e:
    print(e)  # 'MyClass' object has no attribute 'w'

class MyClass:
    def __new__(cls):
        print("__new__ method called")
        return super(MyClass, cls).__new__(cls)

myObj = MyClass()  # __new__ method called

class MyClass:
    instancesAttrs = set()

    def __new__(cls, *args):
        if args not in cls.instancesAttrs:
            cls.instancesAttrs.add(args)
            print("args didn't found. Instance created")
            return super(MyClass, cls).__new__(cls)
        else:
            print("args were found. Instance wasn't created")
            return None

myObj1 = MyClass(0, 0, 0)  # args didn't found...
myObj2 = MyClass(-1, -1, -1)  # args didn't found...
myObj3 = MyClass(0, 0, 0)  # args were found...

print(myObj3)  # None

class MyClass:
    def __setattr__(self, name, value):
        print("__setattr__ method called")

myObj = MyClass()
myObj.x = 0  # __setattr__ method called

class MySubClass(MyClass):
    def __init__(self, x):
        self.x = x  # __setattr__ method called

myObj = MySubClass(1)

class MyClass:
    def __del__(self):
        print("__del__ method called")

myObj = MyClass()
myObj = None  # __del__ method called

class MyClass:
    pass

myObj = MyClass()

print(type(myObj))  # <class '__main__.MyClass'>

print(type(MyClass))  # <class 'type'>

class MyMetaClass(type):
    def __new__(cls, name, bases, dict):
        print("__new__ method called")
        return super().__new__(cls, name, bases, dict)

class MyClass(metaclass=MyMetaClass):  # __new__ method called
    pass

print(type(MyClass))  # <class '__main__.MyMetaClass'>
        