def get_name(addr):
    for i in people:
        if addr == i["address"]:
            return(i["name"])
        raise KeyError

people = [
    {
        'address': 'Funktionstorget 2',
        'name': 'Lena Eriksson'
    },
    {
        'address': 'Listgatan 1',
        'name': 'Erik Olsson'
    },
    {
        'address': 'Strängvägen 3',
        'name': 'Emma Johansson'
    }
]

while True:
    address = input('address > ')

    try:
        print('MATCH:', get_name(address))
    except KeyError:
        print('ERROR: no such address')

    print()