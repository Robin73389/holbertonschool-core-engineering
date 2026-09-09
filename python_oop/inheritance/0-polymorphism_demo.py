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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")
