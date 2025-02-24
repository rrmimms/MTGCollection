from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Subtype
from mtgsdk import Supertype


def get_card():
    print("What would you like to search for?")
    print("1. Card Name")
    print("2. Set Code")
    print("3. Card Type")
    print("4. Mana Cost")
    print("5. Color")
    print("6. Creature Type")
    choice = input("Please enter the number beside your preferred search criterion.")
    if choice == 1:
        criterion = input("What is the card name you'd like to search for?")
        results = Card.where(name = criterion).all()
    if choice == 2:
        criterion = input("What is the set code you'd like to search for?")
        results = Set.where(name = criterion).all()
    if choice == 3:
        criterion = input("What is the card type you'd like to search for?")
        results = Card.where(type = criterion).all()
    if choice == 4:
        criterion = input("What is the mana cost you'd like to search for?")
        results = Card.where(mana_cost = criterion).all()
    if choice == 5:
        criterion = input("What is the card color you'd like to search for?")
        results = Card.where(colors = criterion).all()
    if choice == 6:
        criterion = input("What creature type would you like to search for?")
        results = Card.where(subtype = criterion).all()
    return results