from animal_class import *

class Cow(Animal):
    """A wheat crop"""
    def __init__(self):
        super().__init__(1,7,7)
        self._type = "Calf"
        self._weight = 0

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need and( food > self._food_need) :
                self._weight += self._growth_rate * 1.8
            elif self._status == "Young" and water > self._water_need and( food > self._food_need):
                self._weight += self._growth_rate * 1.55
            elif self._status == "Old" and water > self._water_need and( food > self._food_need):
                self._weight += self._growth_rate / 2
            else:
                self._weight += self._growth_rate

        self._days_growing += 1
        self._update_status()

def main():
    #create a new potato crop
    cow_one = Cow()
    print(cow_one.report())

    manual_grow(cow_one)
    print(cow_one.report())

    manual_grow(cow_one)
    print(cow_one.report())

if __name__ == "__main__":
    main()
