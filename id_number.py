import functools


class NotANineDigitInteger(Exception):
    """
    A class representing an exception of a non integer / integer that has more than 9 digits  
    """

    def __init__(self, arg):
        """
        Initializes the value _arg to arg
        :param arg: representing the argument that raised the exception
        :type arg: can be any type
        :return: None
        """
        self._arg = arg

    def __str__(self):
        """
        returns a message explaining the exception
        """
        msg_error = "The provided input (%s) is not a 9 digit integer" % self._arg
        if type(self._arg) != int:
            msg_error += " and is from type %s" % type(self._arg).__name__
        return msg_error


class IDIterator:
    """
    A class representing an iterator of all the possible ID's
    """

    def __init__(self, id):
        """
        Initializes the value _id to id only if it is a nine digit number
        """
        if len(str(id)) == 9:
            self._id = id

    def __iter__(self):
        """
        Iterator function
        """
        return self

    def __next__(self):
        """
        returning the next ID till 999999999
        :raise: StopIteration raises an exception to stop the iteration
        """
        FLAG = 999_999_999
        if self._id > FLAG:
            raise StopIteration
        while not check_id_valid(self._id):
            self._id += 1
        self._id += 1
        return self._id - 1


def id_generator(id_number):
    """
    Generating the next valid ID starting from the parameter id_number
    :param id_number: the starting point for the ID number
    :type id_number: int
    :yield: the next vallid ID number starting from id_number (including id_number)
    :ytype: int
    """
    while True:
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number
        id_number += 1


def check_id_valid(id_number):
    """
    Checks whether or not the ID number is valid.
    An ID number is valid if the sum of its digits
    is divisible by 10 with no remainder
    where every second digit is multiplied by 2
    (if the product is bigger than 9, the function will calculate the sum of the digits)
    (the function can't accept ID's that start with 0)
    :param id_number: the ID number to check it's validity
    :type id_number: int
    :raise: NotANineDigitInteger : raises an exception if the number is not a nine digit integer
    :return: True if the ID number is valid, False if not
    :rtype: boolean
    """
    # Step 1: make sure that id_number is a 9 digit integer
    try:
        if isinstance(id_number, tuple):
            raise TypeError(id_number)
        elif (not isinstance(id_number, int)) or (len(str(id_number)) != 9):
            raise NotANineDigitInteger(id_number)

    except TypeError:
        return "Can't accept tuples as input"
    except NotANineDigitInteger as e:
        return e

    else:
        # Step 2: check that id_number is actually a valid ID
        '''
        Create a list with the digits of the id number and multiply every second element by 2
        (if the result is bigger than 9, it will be reduced to the sum of the digits):
        '''
        list_after_multiplication = [int(num) if ind % 2 == 0 else sum(
            map(int, str(int(num) * 2))) for ind, num in enumerate(str(id_number))]

        # Sum the whole list to get the final number:
        final_number = functools.reduce(
            lambda x, y: x + y, list_after_multiplication)

        # Step 3: return whether or not the final number is divisible by 10:
        return final_number % 10 == 0

        # COMMENT: can be done in one line like this:
        # return ((functools.reduce(lambda x, y: x + y, [int(num) if ind % 2 == 0 else sum(
        #    map(int, str(int(num) * 2))) for ind, num in enumerate(str(322558297))])) % 10 == 0)


def main():
    FIRST_ID_NUMBER = 123456780
    NUM_OF_IDS = 10
    gen = id_generator(FIRST_ID_NUMBER)
    itr = IDIterator(FIRST_ID_NUMBER)

    # Create temporary files to compare the results
    temp1 = open(r"temporary.txt", 'w')
    temp2 = open(r"temporary2.txt", 'w')

    # Write the ID's to temporary files and print them
    print("Generator:")
    for t1 in range(NUM_OF_IDS):  # pylint: disable = unused-variable
        current_id = (next(gen))
        temp1.write(str(current_id) + "\n")
        print("\t", current_id)

    print("Iterator:")
    for t2 in range(NUM_OF_IDS):  # pylint: disable = unused-variable
        current_id = (next(itr))
        temp2.write(str(current_id) + "\n")
        print("\t", current_id)

    # To compare the results:
    # 1. run the file through the python interactive shell (python -i id_number.py from the terminal)
    # 2. import the function are_files_equal from functions (from functions import are_files_equal)
    # 3. run the following command: are_files_equal(r".\temporary.txt", r".\temporary2.txt")
    # 4. run "rm temporary.txt temporary2.txt" from the terminal to delete the temporary files


if __name__ == "__main__":
    main()
