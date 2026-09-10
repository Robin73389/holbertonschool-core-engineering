#!/usr/bin/env python3
"""ABC class"""
from abc import ABC, abstractclassmethod


# Crée une classe abstract Animal
class Animal(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    @abstractclassmethod
    def sound(self):
        """_summary_
        """
        pass


# Crée une sous class Dog
class Dog(Animal):
    """_summary_

    Args:
        Animal (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Implémenté une method sound()
    def sound(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        # return "Bark"
        return "Bark"


# Crée une sous class Cat
class Cat(Animal):
    """_summary_

    Args:
        Animal (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Implémenté une method sound()
    def sound(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        # return "Meow"
        return "Meow"
