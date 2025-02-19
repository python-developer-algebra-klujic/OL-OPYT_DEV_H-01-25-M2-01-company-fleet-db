'''
Kreirajte bazu s vozilima firme.
ID svakog retka je cijeli broj,
a podaci koji se čuvaju o svakom vozilu su:
tip, proizvođač, registarska oznaka, godina prve registracije te cijena u eur.
'''

# TODO Ako stignemo dio cemo napraviti s funkcijama, a ostatak za DZ, a ako ne onda sve za DZ

import os


STARS = 80


def display_header(menu: str='menu'):
    os.system('cls')
    print()
    print('*'*STARS)
    print()
    print('\tPython Company\' fleet database')
    print()
    print('*'*STARS)

    if menu == 'menu':
        print()
        print(f'Unos podataka o vozilu {id_counter}.')
        print()
    elif menu == 'table':
        print('ID           Tip          Proizvodac      God. proizvodnje   Reg. oznaka      Cijena (EUR)')
        print('_'*STARS)
        print()



# vehicle_type => car, truck, motorcycle, bicycle, agriculture, marine
vehicle = {} # prazan set => set(), a prazan rjecnik samo s viticasatim zagradama {}
vehicle_db = {}
id_counter = 1

# vehicle_db = []
# vehicle_db.append(vehicle) # Dodao sam prazan rjecnik na index 0
# #                               kako bih kasnije mogao dohvatiti prvo vozilo s indeksom 1

while True:
    display_header()

    # TODO Ispisite sve tipove vozila tako da ispred svakog navedete redni broj
    #   Trazite korisnika da selektira jedan broj i tako izabere tip vozila
    vehicle['vehicle_type'] = input('Upisite tip vozila: ')
    vehicle['manufacturer'] = input('Upisite proizvodaca vozila: ')
    vehicle['production_year'] = int(input('Upisite godinu proizvodnje vozila: '))
    vehicle['license_plate'] = input('Upisite registarsku oznaku vozila: ')
    vehicle['purchased_price'] = float(input('Upisite nabavnu cijenu vozila: '))

    # TODO Omogucite korisniku dodavanje svojstva po izboru u rjecnik vehicle
    #       (Hint: razmislite kako dodati novi kljuc u rjecnik)

    # vehicle_db.append(vehicle)
    vehicle_db[id_counter] = vehicle
    id_counter += 1

    next_vehicle = input('Zelite li dodati novo vozilo? (da/ne): ')
    if next_vehicle.lower() != 'da':
        break



# ISPIS PODATAKA O VOZILIMA
display_header('table')

# TODO KReirati funkciju print_database(db_to_print)
# Funkcija mora ispisati bilo koji rjecnik koji se preda kao argument
# ZA ONE KOJI ZELE ZNATI VISE Imate modul koji ispisuje rjecnik u tablicnom formatu.
#   Potrazite na internetu

# Ispis pojedinacnog reda
for id, vehicle in vehicle_db.items():
    print(f'{id}  {vehicle['vehicle_type']}   {vehicle['manufacturer']}   {vehicle['production_year']}   {vehicle['license_plate']}   {vehicle['purchased_price']} EUR')

print()
print('_'*STARS)
print()
