class UniqueInstances:
    __slots__ = []
    instancesAttrs = set()

    def __new__(cls, *args):
        assert len(args) == len(cls.__slots__)
        if  args not in cls.instancesAttrs:
            cls.instancesAttrs.add(args)

            return super(UniqueInstances, cls).__new__(cls)
        else:
            print("Warning: " +
                  "There is another instance of the class " +
                  "'{}'".format(cls.__name__) +
                  " with the same attibutes. The object was not created.")

            return None

    def __init__(self, *args):
        for key, value in zip(self.__slots__, args):
            setattr(self, key, value)

    def __setattr__(self, key, value):
        if hasattr(self, key):
            instanceAttrs = tuple((getattr(self, _key) if _key != key else value
                                  for _key in self.__slots__))
            if instanceAttrs not in self.__class__.instancesAttrs:
                self.__class__.instancesAttrs.\
                    remove(self.instanceAttrs)
                self.__class__.instancesAttrs.add(instanceAttrs)
            else:
                print("Warning: " +
                      "There is another instance of the class " +
                      "'{}'".format(self.__class__.__name__) +
                      " with the same attibutes. The object was not changed.")

                return None

        super(UniqueInstances, self).__setattr__(key, value)

    @property
    def instanceAttrs(self):
        return tuple(getattr(self, key) for key in self.__slots__)

    def __repr__(self):
        return "{}{}".format(self.__class__.__name__, str(self.instanceAttrs))

    def __del__(self):
        self.__class__.instancesAttrs.remove(self.instanceAttrs)

class Coordinate(UniqueInstances):
    __slots__ = ['x', 'y', 'z']

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

    # # view instances' attrs
    # print(Coordinate.instancesAttrs)
    #
    # del first object
    del(coordinate1)

    # view instances' attrs
    print(Coordinate.instancesAttrs)  # set()

    # create second object
    coordinate2 = Coordinate(0, 0, 0)
    coordinate3 = Coordinate(1, 0, 0)
    # print(coordinate2)

    # view instances' attrs
    print(Coordinate.instancesAttrs)  # {(1, 0, 0), (0, 0, 0)}

    # # change value attrs
    # coordinate2.x = 1
    # print(coordinate2)
    #
    # # view instances' attrs
    # print(Coordinate.instancesAttrs)

    # create third object
    # print(coordinate3)

    # # view instances' attrs
    # print(Coordinate.instancesAttrs)
    #
    # change value attrs
    coordinate3.x = 0  # Warning: There is another instance of the class 'Coordinate' with the same attibutes. The object was not changed.
    print(coordinate3)  # Coordinate(1, 0, 0)

    print(UniqueInstances.instancesAttrs)  # {(1, 0, 0), (0, 0, 0)}
    print(Coordinate.instancesAttrs)  # {(1, 0, 0), (0, 0, 0)}
