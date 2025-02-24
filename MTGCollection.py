import pymongo

connection_string = "mongodb+srv://rrmimms:omPUgqwmGiMGZb0D@mtgcollection.5wlvw.mongodb.net/?retryWrites=true&w=majority&appName=MTGCollection"
client = pymongo.MongoClient(connection_string)
db = client["MTGCollection"]
collections = db["My_Collection"]


def add_card(card):
    collections.insert_one(card)

def input_card():
    number_to_add = int(input("How many cards do you want to add? "))
    for i in range(number_to_add):
        card = {}
        card["name"] = input("Enter the name of the card: ")
        card["set"] = input("Enter the set of the card: ")
        card["quantity"] = int(input("Enter the quantity of the card: "))
        card["foil"] = input("Is the card foil? (True/False): ")
        card["price"] = float(input("Enter the price of the card: "))
        add_card(card)
        for key, value in card.items():
            print(f"{key}: {value}")
    print("Cards added to collection")

def get_collection():
    for card in collections.find():
        print(card)

def get_card():
    name = input("Enter the name of the card you want to find: ")
    card = collections.find_one({"name": name})
    print(card)

def update_card():
    name = input("Enter the name of the card you want to update: ")
    card = collections.find_one({"name": name})
    print(card)
    field = input("Enter the field you want to update: ")
    value = input(f"Enter the new value for {field}: ")
    collections.update_one({"name": name}, {"$set": {field: value}})
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
        print("1. Add a card")
        print("2. Get collection")
        print("3. Get card")
        print("4. Update card")
        print("5. Delete card")
        print("6. Exit")
        choice = int(input("Enter the number of the action you want to perform: "))
        if choice == 1:
            input_card()
        elif choice == 2:
            get_collection()
        elif choice == 3:
            get_card()
        elif choice == 4:
            update_card()
        elif choice == 5:
            delete_card()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
    print("Goodbye!")
main()