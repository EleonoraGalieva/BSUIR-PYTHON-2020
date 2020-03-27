class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Car(metaclass=Singleton):

    def __init__(self, model):
        self.model = model


# И 1 и 2 машины будут Ford
car1 = Car("Ford")
car2 = Car("Nissan")
