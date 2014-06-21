from animal_class import *

class Sheep(Animal):
    """A sheep"""
    def __init__(self,name):
        super().__init__(1,5,9,name)
        self._type = "Sheep"
        self._weight = 0

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Baby" and water > self._water_need and( food > self._food_need) :
                self._weight += self._growth_rate * 1.7
            elif self._status == "Young" and water > self._water_need and( food > self._food_need):
                self._weight += self._growth_rate * 1.6
            elif self._status == "Old" and water > self._water_need and( food > self._food_need):
                self._weight += self._growth_rate / 2
            else:
                self._weight += self._growth_rate

        self._days_growing += 1
        self._update_status()

def get_name():
    valid = False
    while not valid:
        name = input("Please enter a name: ")
        if len(name) > 0:
            valid = True
        else:
            print("Please enter a name. ")
    return name

def main():
    #create a new potato crop
    name = get_name()
    sheep_one = Sheep(name)
    print(sheep_one.report())

    manual_grow(sheep_one)
    print(sheep_one.report())

    manual_grow(sheep_one)
    print(sheep_one.report())

if __name__ == "__main__":
    main()
