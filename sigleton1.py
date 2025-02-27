class Singleton:
    _instance = None

    def new(cls):
        if cls._instance is None:
            cls._instance = super().new(cls)
        return cls._instance
    

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)