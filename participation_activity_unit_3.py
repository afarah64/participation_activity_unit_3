""" this program generates random names by combining names and adjectives from two lists.
author: Abdalla Farah
Date: 01/30/2026
    
"""
import random

names: list[str]=["grugur", "kouvok", "lethik", "broulos", "kaugan", "chaelazar", "raelazar", "dacular", "pazhar", "drukras"]
adjectives: list[str]=["bane", "the resurrector", "the decayer", "the corpse", "bane", "the living", "the resurrector", "graeme", "the abomination", " "]

for i in range(len(names)):
    name = names.pop(random.randint(0, len(names)-1)).title()
    adjective = adjectives.pop(random.randint(0, len(adjectives)-1)).title()
    print(f"\n Name generator:\n \t {name} {adjective}\n")

   