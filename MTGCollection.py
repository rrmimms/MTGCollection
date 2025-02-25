import time

import pymongo
import configparser
import CardSearch

config = configparser.ConfigParser()
config.read("config.ini")

mongo_key = config["section1"]["mongo_key"]

connection_string = mongo_key
client = pymongo.MongoClient(connection_string)
db = client["MTGCollection"]
collections = db["My_Collection"]

def search_card():
    card = CardSearch.get_card()
    for key, value in card.items():
        print(f"{key} : {value}")
    print(card)
    print("Would you like to add this card to your collection?")
    add = input("Y/N: ")
    if add == "Y":
        add_card(card)
        print("Card added to collection")
    else:
        print("Card not added to collection")

def add_card(card):
    collections.insert_one(card)

def input_cards():
    number_to_add = int(input("How many cards do you want to add? "))
    for i in range(number_to_add):
        card = {"name": input("Enter the name of the card: "), "set": input("Enter the set of the card: "),
                "quantity": int(input("Enter the quantity of the card: ")),
                "foil": input("Is the card foil? (True/False): "),
                }
        card["price"] = CardSearch.get_price(card["name"])
        add_card(card)
        for key, value in card.items():
            print(f"{key}: {value}")
    print("Cards added to collection")

def get_collection():
    for card in collections.find():
        card["price"] = CardSearch.get_price(card["name"])
        print(card)
        time.sleep(.1)

def get_card():
    name = input("Enter the name of the card you want to find: ")
    card = collections.find_one({"name": name})
    card["price"] = CardSearch.get_price(name)
    print(card)

def update_card():
    name = input("Enter the name of the card you want to update: ")
    card = collections.find_one({"name": name})
    print(card)
    field = input("Enter the field you want to update: ")
    value = input(f"Enter the new value for {field}: ")
    collections.update_one({"name": name}, {"$set": {field: value}})
    card["price"] = CardSearch.get_price(name)
    print("Card updated")

def delete_card():
    name = input("Enter the name of the card you want to delete: ")
    card = collections.find_one({"name": name})
    print(card)
    confirm = input("Are you sure you want to delete this card? (Y/N) ")
    if confirm == "Y":
        collections.delete_one({"name": name})
        print("Card deleted")
    else:
        print("Card not deleted")

def main():
    print("Welcome to the MTG Collection Manager")
    while True:
        print("1. Add cards to collection")
        print("2. Get collection")
        print("3. Get card")
        print("4. Update card")
        print("5. Delete card")
        print("6. Search Card")
        print("7. Price Search")
        print("8. Exit")
        choice = int(input("Enter the number beside the action you want to perform: "))
        if choice == 1:
            input_cards()
        elif choice == 2:
            get_collection()
        elif choice == 3:
            get_card()
        elif choice == 4:
            update_card()
        elif choice == 5:
            delete_card()
        elif choice == 6:
            CardSearch.get_card()
        elif choice == 7:
            term = input("Please enter the name of the card you'd like pricing data for.")
            print(CardSearch.get_price(term))
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")
    print("Goodbye!")
main()
