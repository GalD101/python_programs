# 2.2.2
from re import search, compile
from string import punctuation


class Octopus:

    count_animals = 0

    def __init__(self, age, name='Octavio'):
        self._age = age
        self._name = name
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Pixel:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        colors_avg = (self._red + self._green + self._blue) / 3
        self._red = colors_avg
        self._green = colors_avg
        self._blue = colors_avg

    def print_pixel_info(self):
        info = 'X: %d, Y: %d, Color: (%d, %d, %d)' % (
            self._x, self._y, self._red, self._green, self._blue)
        if self._red == 0 and self._green == 0 and self._blue != 0:
            info += ' Blue'
        elif self._red == 0 and self._green != 0 and self._blue == 0:
            info += ' Green'
        elif self._red != 0 and self._green == 0 and self._blue == 0:
            info += ' Red'
        print(info)


class BigThing:
    def __init__(self, obj):
        self._obj = obj

    def size(self):
        if isinstance(self._obj, int) or isinstance(self._obj, float):
            return self._obj
        return len(self._obj)


class BigCat(BigThing):
    def __init__(self, obj, weight):
        super().__init__(obj)
        self._weight = weight

    def size(self):
        if self._weight > 20:
            return "Very Fat"
        elif self._weight > 15:
            return "Fat"
        return 'OK'


class UnderAge(Exception):

    def __init__(self, age):
        self._age = age

    def __str__(self):
        age = self._age
        years_left = 18 - self._age
        message = f"{age} is under age. you will be invited in {years_left} years"
        if years_left == 1:
            return message[:-1]
        else:
            return message


def main():
    pass


if __name__ == "__main__":
    main()
