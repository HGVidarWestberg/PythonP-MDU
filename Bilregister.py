
# Gruppuppgift 2 – Bilregistret
#
# Steg 1: Fyll i get_owner. Testa med ABC123.
# Steg 2: Lägg till try/except så att programmet inte kraschar när
# regnumret saknas. Skriv då ut: ERROR: no such car
#
# Utmaning 1: abc123 ska också fungera (små bokstäver).
# Utmaning 2: Skriv get_cars(owner) som returnerar en lista med alla
# regnummer som ägaren har. Testa med 'Anna Berg'.
cars = [
{'reg': 'ABC123', 'owner': 'Anna Berg'},
{'reg': 'XYZ789', 'owner': 'Johan Lind'},
{'reg': 'DEF456', 'owner': 'Maria Holm'},
{'reg': 'GHI321', 'owner': 'Anna Berg'},
]

def get_owner(reg: str) -> str:
    """Returnerar ägaren till bilen med registreringsnumret reg.
    Lyfter KeyError om regnumret inte finns i cars.
    """

    for car in cars:
        if car["reg"].lower() == reg.lower():
            return car["owner"]
    raise IndexError

def get_cars(owner: str) -> list:
    OwnedCars = []
    for car in cars:
        if car["owner"] == owner:
            OwnedCars.append(car["reg"])
    if len(OwnedCars) > 0:
        return OwnedCars
    else:
        raise IndexError

while True:
    # owner = input("Ägare: ")
    # try: 
    #     reg = get_cars(owner)
    #     print(reg)
    # except IndexError:
    #     print("No cars")


    reg = input('Regnummer: ')
    try:
        owner = get_owner(reg)
        print(owner)
    except IndexError:
        print("no such car")