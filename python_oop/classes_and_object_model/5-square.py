#!/usr/bin/env python3
"""Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size ** 2

    def my_print(self):
        """_summary_
        """
        if self.size == 0:
            print("\n")
        else:
            for i in range(self.size):
                print("#" * self.size)
