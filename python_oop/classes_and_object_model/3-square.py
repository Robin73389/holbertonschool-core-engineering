#!/usr/bin/env python3
"""Square class"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        area = self.__size * self.__size
        return area
