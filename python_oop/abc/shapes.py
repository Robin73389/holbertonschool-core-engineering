#!/usr/bin/env python3
"""Shape"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def area(self):
        """_summary_
        """
        pass

    @abstractmethod
    def perimeter(self):
        """_summary_
        """
        pass


class Circle(Shape):
    """_summary_

    Args:
        Shape (_type_): _description_
    """
    def __init__(self, radius):
        """_summary_

        Args:
            radius (_type_): _description_
        """
        self.radius = radius

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """_summary_

    Args:
        Shape (_type_): _description_
    """
    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.width = width
        self.height = height

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width * self.height

    def perimeter(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return 2 * (self.width + self.height)


def shape_info(info):
    """_summary_

    Args:
        info (_type_): _description_
    """
    print(info.area())
    print(info.perimeter())
