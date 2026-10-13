import requests
import json

BASE_URL = "https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com"

def list_cities() -> list[str]:
    """Hämtar alla städer.
    Anropar resursen / och plockar ut listan.
    Params:
    Inga
    Returns:
    En lista med städer.
    """

    response = requests.get(BASE_URL + "/")
    data = response.json()
    return data["cities"]

def list_users(city: str) -> list[dict]:
    """Hämtar alla användare i en stad.
    Anropar resursen /{city} och plockar ut listan under nyckeln "users".
    Params:
    city: stadens namn, t.ex. "stockholm".
    Returns:
    En lista med användare. Varje användare är ett dictionary med
    nycklarna "id", "forename" och "surname".
    """
    response = requests.get(BASE_URL+"/"+city)
    return response.json()["users"]

def get_user(city: str, user_id: str) -> dict:
    """Hämtar all information om en användare, inklusive användarens djur.
    Anropar resursen /{city}/{user_id}.
    Params:
    city: stadens namn, t.ex. "stockholm".
    user_id: användarens id, som du får från list_users().
    Returns:
    Ett dictionary med nycklarna "id", "city", "forename", "surname"
    och "animals". Värdet för "animals" är en lista där varje djur är
    ett dictionary med nycklarna "name", "age" och "type".
    """
    response = requests.get(BASE_URL+"/"+city+"/"+user_id)
    return response.json()

def count_users(city: str):
    """Anger hur många användare som är från en stad.
    Params:
    city: stadens namn, t.ex. "stockholm".
    Returns:
    En integer som beskriver användarna i en stad
    """

    response = list_users(city)
    return len(response)

def list_pets(city: str, type: str, age: int):
    response = list_users(city)
    returnlist = []
    for item in response:
        person = requests.get(BASE_URL+"/"+city+"/"+item["id"]).json()
        animals = person["animals"]
        for pet in animals:
            if pet["age"] == age and pet["type"] == type:
                returnlist.append(pet["name"] + ", " + str(pet["age"]) + "år - ägare: " + person["forename"] + " " + person["surname"])
    return returnlist

while True:
    stad = input("city > ").lower()
    djur = input("animal > ").lower()
    ålder = int(input("age > "))
    print("")

    städer = list_cities()
    if stad not in städer:
        print("ERROR: city not found")
        continue

    pet_list = list_pets(stad, djur, ålder)

    if len(pet_list) == 0:
        print("inga djur hittades")
    else: 
        for item in pet_list:
            print(item)
