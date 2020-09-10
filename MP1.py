# -*- coding: utf-8 -*-
# le \ permet de continuer la ligne précédentes à la ligne suivantes
# les il signifie le programme


"""mini projet 1 de 2020 - 2021"""


import re


import math as m
import random as rdm


def ask_number(text: str = "") -> float:
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


def sapin_de_noel(n: int) -> None:
    j = 1
    for i in range(1, n + 1):
        print("".join(["^"] * j).center(2 * n))
        j += 2


def merci_la_france() -> None:
    rep = ask_number("prix (0 pour arrêter) = ")
    while rep != 0:
        print(rep * 1.20)
        rep = ask_number("prix (0 pour arrêter) = ")


def amende(victimes: str) -> None:

    def prix(victimes) -> int:
        victimes_l = [int(i) for i in victimes.split(" ")]
        print(victimes_l)
        prix = [1, 3, 5, 10]
        nb_point = 0
        for i in range(len(victimes_l)):
            nb_point += victimes_l[i] * prix[i]
        return m.ceil(nb_point / 100) * 200

    victs = input("victimes = ")
    while not re.findall(r"^\d+ \d+ \d+ \d+$", victs):
        victs = input("victimes = ")
    print(amende(victs))


def haruri() -> None:
    ha_weight = ask_number()
    ha_food_weight = ask_number()
    ha_ratio = ha_food_weight / ha_weight
    number_animals = int(ask_number())
    return_val = 0
    for i in range(number_animals):
        stat_animal = input()
        while not re.findall(r"^\d+ \d+$", stat_animal):
            stat_animal = input()
        animal_weight, animal_food_weight = stat_animal.split(" ")
        animal_ratio = int(animal_food_weight) / int(animal_weight)
        if animal_ratio > ha_ratio:
            return_val += 1
    print(return_val)


def analyse_adn() -> None:

    def nb_seq(adn: str, sequeance: str) -> int:
        nmb_seq = len(re.findall(sequeance, adn))
        return nmb_seq

    adn_in = input("chaine : ")
    seq = input("seq : ")

    print(
                "Il y a {} % de {} dans votre chaine"
                .format(
                        round(nb_seq(adn_in, seq) / len(adn_in) * 100, 2),
                        repr(seq)
                    )
            )


if __name__ == "__main__":
    # print(vol_col_droit(3, 3))
    # roulette_100()
    # sapin_de_noel(12)
    # haruri()
    analyse_adn()
    pass
