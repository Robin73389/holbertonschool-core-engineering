#!/usr/bin/env python3
"""Square class"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            TypeError: _description_
            ValueError: _description_
            ValueError: _description_
        """
        try:
            if not isinstance(size, int):
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")

        try:
            if size < 0:
                raise ValueError
        except ValueError:
            raise ValueError("size must be >= 0")

        self.__size = size
