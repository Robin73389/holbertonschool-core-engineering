#!/usr/bin/env python3

def replace_in_list(my_list, idx, element):
    """_summary_

    Args:
        my_list (_type_): _description_
        idx (_type_): _description_
        element (_type_): _description_

    Returns:
        _type_: _description_
    """
    if idx < 0 or idx > len(my_list):
        return my_list

    else:
        my_list[idx] = element
        return my_list
