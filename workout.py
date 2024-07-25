class Workout:
    def __init__(self, duration, distance):
        self.duration = duration
        self.distance = distance

    def display_workout(self):
        print(f"{self.__class__.__name__}: distance [{self.distance}] duration[{self.duration}]")

    def get_class_name(self):
        return self.__class__.__name__

class Running(Workout):
    pass

class Biking(Workout):
    pass

class Swimming(Workout):
    pass