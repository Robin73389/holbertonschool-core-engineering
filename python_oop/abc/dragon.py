#!/usr/bin/env python3
"""Dragon"""


class SwimMixin:
    """_summary_
    """
    def swim(self):
        """_summary_
        """
        print("The creature swims!")


class FlyMixin:
    """_summary_
    """
    def fly(self):
        """_summary_
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """_summary_

    Args:
        SwimMixin (_type_): _description_
        FlyMixin (_type_): _description_
    """
    def roar(self):
        """_summary_
        """
        print("The dragon roars!")
