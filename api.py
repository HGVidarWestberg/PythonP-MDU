"""Jet Set Pets
API-dokumentation: sidan "Jet Set Pets [dokumentation]" på Canvas.
"""
import requests
BASE_URL = "https://8fzqlwv0jd.execute-api.eu-north-1.amazonaws.com"
def list_cities() -> list[str]:
    """Hämtar alla städer som finns i Jet Set Pets.
    Anropar resursen / och plockar ut listan under nyckeln "cities".
    Returns:
    En lista med städernas namn, t.ex. ["stockholm", "uppsala"].
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
# UPPGIFT 1a: Skriv din kod här (och ta bort pass).
pass
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
# UPPGIFT 1b: Skriv din kod här (och ta bort pass).
pass
# UTMANING 1: Skriv en egen funktion count_users(city) som returnerar
# antalet användare i en stad. Glöm inte type hints och docstring!
# ======================================================================
# TESTA UPPGIFT 1
# Ta bort # framför raderna nedan när list_users och get_user är klara,
# och kör filen ( ).▷
# Inför block 2: sätt # framför alla testrader igen.
# ======================================================================
print("TEST list_cities:", list_cities())
# users = list_users("stockholm")
# print("TEST list_users:", users[:3])
# print("TEST get_user:", get_user("stockholm", users[0]["id"]))
# ======================================================================
# BLOCK 2 · UPPGIFT 2: DJURFINNAREN
# Fråga användare efter stad, djurtyp och ålder.
# Skriv ut alla djur i staden som # har både den typen och den åldern,
# tillsammans med ägarens namn.
#
# Tänk först: vilket anrop görs en gång, och vilket görs en gång per varv?
# Testa med några få användare först, t.ex. users[:5].
#
# Utmaning: skriv "Inga djur hittades" om inget djur matchar, och
# "ERROR: city not found" om staden inte finns.
# ======================================================================
