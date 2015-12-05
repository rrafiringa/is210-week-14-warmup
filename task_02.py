#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Week 14 Task 02 """

from data import FRUIT


def get_cost_per_item(shoplist):
    """
    Args:
        shoplist (dict):  Shopping list
    Returns:
        dict: Fruit total cost per item keyed by fruits
    Examples:
        >>> get_cost_per_item({'Black Plum': 8,
                               'Bosc Pear': 4})
        {'Bosc Pear': 7.96, 'Black Plum': 23.92}
    """
    return {key: numfruits * FRUIT[key] for key,
            numfruits in shoplist.iteritems() if key in FRUIT.keys()}


def get_total_cost(shoplist):
    """
    Args:
        shoplist (dict): Shopping list
    Returns:
        Numeric: Total cost of all items
    Examples:
        >>> get_total_cost({'Black Plum': 8,
                            'Bosc Pear': 4})
    """
    return sum(get_cost_per_item(shoplist).itervalues())


if __name__ == '__main__':
    LIST = {'Black Plum': 8,
            'Bosc Pear': 4}
    print get_cost_per_item(LIST)
    print get_total_cost(LIST)