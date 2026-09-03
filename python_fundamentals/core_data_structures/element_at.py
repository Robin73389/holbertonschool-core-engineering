#!/usr/bin/env python3

def element_at(my_list, idx):
    """_summary_

    Args:
        my_list (_type_): _description_
        idx (_type_): _description_

    Returns:
        _type_: _description_
    """
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
