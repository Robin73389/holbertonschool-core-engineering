#!/usr/bin/env python3

def best_score(a_dictionary):
    """_summary_

    Args:
        a_dictionary (_type_): _description_

    Returns:
        _type_: _description_
    """
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get)
