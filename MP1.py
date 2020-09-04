# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


"""mini projet 1 de 2020 - 2021"""


import math as m
import random as rdm


def ask_number(text: str) -> float:
    assert isinstance(text, str), \
        "text not str but {}".format(type(text))

    return_val: str = input(text)
    while not return_val.isdigit():
        return_val: str = input(text)

    return_val: float = float(return_val)

    return return_val


def vol_col_droit(r: int or float, h: int or float) -> float:
    assert isinstance(r, (int, float)), \
        "r not int or float but {}".format(type(r))
    assert isinstance(h, (int, float)), \
        "h not int or float but {}".format(type(h))

    return_val: float = m.pi * (r ** 2) * h / 3

    assert isinstance(return_val, float), \
        "return_val not float but {}".format(type(return_val))

    return return_val


def roulette_100() -> None:
    def comparaison(val: int, user_val: int) -> bool:
        return_val: bool = True
        if user_val < val:
            print("Trop petit!")
        elif user_val > val:
            print("Trop grand!")
        else:
            return_val: bool = False

        return return_val

    def verif_uv(
            ) -> int:

        verif_uv = ask_number("combien compris entre 1 et 100 = ")
        while verif_uv < 1 and verif_uv > 100:
            verif_uv = ask_number("combien compris entre 1 et 100 = ")

        verif_uv: int = int(verif_uv)

        return verif_uv

    i: int = 1
    value: int = rdm.randint(1, 100)
    users_value: int = int(verif_uv())

    while comparaison(value, users_value):
        users_value = verif_uv()
        i += 1
    print("Gagné en " + str(i) + (" coups", " coup")[i == 1])


if __name__ == "__main__":
    print(vol_col_droit(3, 3))
    roulette_100()
