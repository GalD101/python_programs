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


class UsernameContainsIllegalCharacter(Exception):

    def __init__(self, user_name):
        self._user_name = user_name

    def __str__(self):
        return "'%s' contains illegal character(s) user name" % self._user_name


class UsernameTooShort(Exception):

    def __init__(self, user_name):
        self._user_name = user_name

    def __str__(self):
        return "'%s' is too short (%d character(s) long) and it should contain " \
               "3 - 16 characters" % self._user_name, len(self._user_name)


class UsernameTooLong(Exception):

    def __init__(self, user_name):
        self._user_name = user_name

    def __str__(self):
        return "'%s' is too long (%d characters long)" % self._user_name, len(self._user_name)


class PasswordMissingCharacter(Exception):

    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "your password (%s) is missing a unique character" % self._password


class PasswordTooShort(Exception):

    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "'%s' is too short (%d character(s) long) and it should contain " \
               "8 - 40 characters" % self._password, len(self._password)


class PasswordTooLong(Exception):

    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "'%s' is too long (%d characters long) and it should contain " \
               "8 - 40 characters" % self._password, len(self._password)


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


def check_input(username, password):
    """#TODO add documentation"""
    UNDER_LINE = '_'
    USERNAME_LENGTH = len(username)
    PASSWORD_LENGTH = len(password)
    try:
        if (username.find(UNDER_LINE) == -1) or (search('[a-zA-Z]+', username) \
            is None) or (search(r'\d', username) is None):
            raise UsernameContainsIllegalCharacter(username)
        if USERNAME_LENGTH < 3:
            raise UsernameTooShort(username)
        if USERNAME_LENGTH > 16:
            raise UsernameTooLong(username)
        if search('[a-zA-Z]', password == None) and search('\d', password == None):
            pass
        if PASSWORD_LENGTH < 8:
            raise PasswordTooShort(password)
        if PASSWORD_LENGTH > 40:
            raise PasswordTooLong(password)
    except UsernameContainsIllegalCharacter:
        print(UsernameContainsIllegalCharacter)
    except UsernameTooShort as e:
        print(e)
    except UsernameTooLong as e:
        print(e)
    except PasswordMissingCharacter as e:
        print(e)
    except PasswordTooShort as e:
        print(e)
    except PasswordTooLong as e:
        print(e)
    else:
        print("OK")

def main():
    pass

if __name__ == "__main__":
    main()
