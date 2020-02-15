class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """Initializes the values name and hunger so that hunger default value is 0.
        :param name: the name associated with the animal
        :param hunger: the hunger level of the animal (if no value is given the value will be 0)
        :type name: string
        :type hunger: int
        :return: None
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        """Returns true if the animal is hungry (if hunger level > 0)
        :return: whether or not the animal is hungry
        :rtype: boolean
        """
        return self._hunger > 0

    def feed(self):
        """Decreases the hunger level of the animal by 1.
        """
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def __init__(self, name, hunger):
        """Initializes the values name and hunger so that hunger default value is 0.
        :param name: the name associated with the dog
        :param hunger: the hunger level of the dog (if no value is given the value will be 0)
        :type name: string
        :type hunger: int
        :return: None
        """
        Animal.__init__(self, name, hunger)

    # Overriding method
    def talk(self):
        """Makes the dog say "woof woof"
        """
        print("woof woof")

    # Unique method
    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def __init__(self, name, hunger):
        """Initializes the values name and hunger so that hunger default value is 0.
        :param name: the name associated with the cat
        :param hunger: the hunger level of the cat (if no value is given the value will be 0)
        :type name: string
        :type hunger: int
        :return: None
        """
        Animal.__init__(self, name, hunger)

    # Overriding method
    def talk(self):
        """Makes the cat say "meow"
        """
        print("meow")

    # Unique method
    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        """Initializes the values name, hunger and stink_count so that\
            hunger default value is 0 and stink_count default value is 6.
        :param name: the name associated with the skunk
        :param hunger: the hunger level of the skunk (if no value is given the value will be 0)
        :param stink_count: the stink counter for the skunk (if no value is given the value will be 6)
        :type name: string
        :type hunger: int
        :type stink_count: int
        :return: None
        """
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    # Overriding method
    def talk(self):
        """Makes the skunk say "tsssss"
        """
        print("tsssss")

    # Unique method
    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger):
        """Initializes the values name and hunger so that hunger default value is 0.
        :param name: the name associated with the unicorn
        :param hunger: the hunger level of the unicorn (if no value is given the value will be 0)
        :type name: string
        :type hunger: int
        :return: None
        """
        Animal.__init__(self, name, hunger)

    # Overriding method
    def talk(self):
        """Makes the unicorn say "Good day, darling"
        """
        print("Good day, darling")

    # Unique method
    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        """Initializes the values name, hunger and color so that \
            hunger default value is 0 and color default value is Green.
        :param name: the name associated with the dragon
        :param hunger: the hunger level of the dragon (if no value is given the value will be 0)
        :param color: the color of the dragon (if no value is given the value will be "Green")
        :type name: string
        :type hunger: int
        :type color: string
        :return: None
        """
        Animal.__init__(self, name, hunger)
        self._color = color

    # Overriding method
    def talk(self):
        """Makes the dragon say "Raaaawr"
        """
        print("Raaaawr")

    # Unique method
    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky", 0), Unicorn("Keith", 7),
               Dragon("Lizzy", 1450), Dog("Doggo", 80), Cat(
                   "Kitty", 80), Skunk("Stinky Jr.", 80),
               Unicorn("Clair", 80), Dragon("McFly", 80)]

    # Iterate over the animals in the zoo
    for animal in zoo_lst:

        # print the animal's type and name
        print(type(animal).__name__, animal.get_name())

        # Feed the animal until it's full
        while animal.is_hungry():
            animal.feed()
        animal.talk()

        # Call the animal's unique method
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print("Zoo name:", Animal.zoo_name)


if __name__ == "__main__":
    main()
