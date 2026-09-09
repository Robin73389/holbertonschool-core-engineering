#!/usr/bin/env python3
"""BaseGeometry"""


class BaseGeometry:
    """Clas BaseGeometry"""
    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")

        self.integer_validator()


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width * self.__height

    def print():
        """_summary_
        """
        print()

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
