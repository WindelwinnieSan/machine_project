"""
Einstiegs-Datei in das Machine-Projekt
Informationen ücer das Betriebssystem mit dme platform - Modul
"""

# import this  # Zen of python importieren
import sys
import random


import check

# Mit folgendem Statement wird auch das ganze Modul importiert, es gewährt aber
# nur Zugriff auf die Funktion hello_again
from check import hello_again

# from copy import deepcopy  # Ist üblich, da deepcopy schon aussagt, aus welchem

# das infos-Modul aus Package library importieren
from library import infos


def main():
    # gebe die Infos für das OS aus
    print("*" * 40)
    print("System Infos")
    print("Computer Name:", infos.computer_name())  # data
    print("Operating System:", infos.operating_system())
    print("Processor:", infos.cpu())
    print("Machine:", infos.machine())
    print("Python Version:", infos.version())  # ('3', '11', '3')  Major Minor Patch
    print(
        "Python Interpreter:", infos.implementation()
    )  # CPython / Micropython / Pypython
    print("System und Version:", infos.system())
    print("*" * 40)


# random.randint(3,4)   # Zugriff über random-Namespace
# check Namespace via Dot-Notation
check.say_hello()
hello_again()

# an diesen Orten sucht Python nach einem Modul
print(sys.path)

# diese Module sind schon geladen
print("*" * 40)
# for key, value in sys.modules.items():
#     print(key, value)

main()
