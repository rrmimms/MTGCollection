from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Subtype
from mtgsdk import Supertype
import requests
import json


headers = {
        "User_Agent" : "MTGCollection/1.0",
        "Accept" : "application/json"
    }

def get_price(name):
    response = requests.get("https://api.scryfall.com/cards/named?fuzzy=" + name, headers = headers)
    searchedCard = response.json()
    return searchedCard["prices"]

def get_card():
    print("What would you like to search for?")
    print("1. Card Name")
    print("2. Set Code")
    print("3. Card Type")
    print("4. Mana Cost")
    print("5. Color")
    print("6. Creature Type")
    print("7. Card Price")
    choice = int(input("Please enter the number beside your preferred search criterion."))
    if choice == 1:
        term = input("What is the card name you'd like to search for?")
        results = Card.where(name = term).all()
    elif choice == 2:
        term = input("What is the exact set code you'd like to search for?")
        results = Set.where(name = term).all()
    elif choice == 3:
        term = input("What is the card type you'd like to search for?")
        results = Card.where(types = term).all()
    elif choice == 4:
        term = input("What is the mana cost you'd like to search for?")
        results = Card.where(mana_cost = term).all()
    elif choice == 5:
        term = input("What is the card color you'd like to search for?")
        results = Card.where(colors = term).all()
    elif choice == 6:
        term = input("What creature type would you like to search for?")
        results = Card.where(subtype = term).all()
    elif choice == 7:
        term = input("What card would you like to find prices for?")
        results = get_price(term)
    return results

def by_card_type():
    return 1