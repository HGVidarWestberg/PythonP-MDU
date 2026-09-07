a = {"sweden":{"food": "ica", "construction": "skanska ab"},
     "usa":{"food": "walmart", "construction": "bechtel group inc"}}

while True:
    country = input("country(sweden/usa): ").lower()
    try:
        if country == "sweden" or country == "usa":
            break
        else:
            print("invalid country, try again")
    except: 
        print("invalid country, try again")

while True:
    sector = input("sector(food/construction): ").lower()
    try:
        if sector == "food" or sector == "construction":
            break
        else:
            print("invalid sector, try again")
    except:
        print("invalid sector, try again")

print("your company is:", a[country][sector])