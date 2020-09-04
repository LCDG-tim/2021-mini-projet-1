# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


"""mini projet 1 de 2020 - 2021"""


import math as m


def vol_col_droit(r: int or float, h: int or float) -> float:
    assert isinstance(r, (int, float)), \
        "r not int or float but {}".format(type(r))
    assert isinstance(h, (int, float)), \
        "h not int or float but {}".format(type(h))

    return_val: float = m.pi * (r ** 2) * h / 3

    assert isinstance(return_val, float), \
        "return_val not float but {}".format(type(return_val))

    return return_val


if __name__ == "__main__":
    print(vol_col_droit(3, 3))
