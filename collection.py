class UniqueInstances(type):
    def init(self, *args):
        for key, value in zip(self.__slots__, args):
            setattr(self, key, value)

    def setattr(self, key, value):
        if hasattr(self, key):
            _instanceAttr = tuple((getattr(self, _key)
                                   if _key != key else value
                                   for _key in self.__slots__))

            if _instanceAttr not in self.__class__.instancesAttrs:
                self.__class__.instancesAttrs.\
                    remove(self.instanceAttrs)
                self.__class__.instancesAttrs.add(_instanceAttr)
            else:
                print("Warning: " +
                      "There is another instance of the class " +
                      "'{}'".format(self.__class__.__name__) +
                      " with the same attibutes. The object was not changed.")

                return None

        object.__setattr__(self, key, value)

    def get_instancesAttr(self):
        return tuple(getattr(self, key) for key in self.__slots__)

    def repr(self):
        return "{}{}".format(self.__class__.__name__, str(self.instanceAttrs))

    def delete(self):
        self.__class__.instancesAttrs.remove(self.instanceAttrs)

    def __new__(cls, name, bases, dict):
        dict['instancesAttrs'] = set()
        dict['__init__'] = UniqueInstances.init
        dict['__setattr__'] = UniqueInstances.setattr
        dict['instanceAttrs'] = property(UniqueInstances.get_instancesAttr)
        dict['__repr__'] = UniqueInstances.repr
        dict['__del__'] = UniqueInstances.delete

        return super().__new__(cls, name, bases, dict)

    def __call__(cls, *args):
        assert len(args) == len(cls.__slots__)

        if args not in cls.instancesAttrs:
            cls.instancesAttrs.add(args)

            return super().__call__(*args)
        else:
            print("Warning: " +
                  "There is another instance of the class " +
                  "'{}' ".format(cls.__name__) +
                  "with the same attributes. The object was not created.")

            return None

class Coordinate(metaclass=UniqueInstances):
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        super(Coordinate, self).__init__(x, y, z)


if __name__ == "__main__":
    # view instances' attrs
    print(Coordinate.instancesAttrs)  # set()

    # instantiates first object
    coordinate1 = Coordinate(0, 0, 0)
    print(coordinate1)  # Coordinate(0, 0, 0)
    
    # try to add a attr to first object
    try:
        coordinate1.a = 1
    except Exception as e:
        print(e)  # 'Coordinate' object has no attribute 'a'
    
    # view instances' attrs
    print(Coordinate.instancesAttrs)
    
    # try instantiates second object with attrs first object
    coordinate2 = eval(repr(coordinate1))  # Warning: There is another instance of the class 'Coordinate' with the same attibutes. The object was not created.
    print(coordinate2)  # None
    
    # view instances' attrs
    print(Coordinate.instancesAttrs)
    
    # del first object
    del(coordinate1)
    
    # view instances' attrs
    print(Coordinate.instancesAttrs)  # set()
    
    # create second object
    coordinate2 = Coordinate(0, 0, 0)
    coordinate3 = Coordinate(1, 0, 0)
    print(coordinate2)
    
    # view instances' attrs
    print(Coordinate.instancesAttrs)  # {(1, 0, 0), (0, 0, 0)}
    
    # change value attrs
    coordinate2.x = 1
    print(coordinate2)
    
    # view instances' attrs
    print(Coordinate.instancesAttrs)
    
    # create third object
    print(coordinate3)
    
    # view instances' attrs
    print(Coordinate.instancesAttrs)
    
    # change value attrs
    coordinate3.x = 0  # Warning: There is another instance of the class 'Coordinate' with the same attibutes. The object was not changed.
    print(coordinate3)  # Coordinate(1, 0, 0)
