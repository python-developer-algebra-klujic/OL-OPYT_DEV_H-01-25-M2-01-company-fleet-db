'''
Kreirajte bazu s vozilima firme.
ID svakog retka je cijeli broj,
a podaci koji se čuvaju o svakom vozilu su:
tip, proizvođač, registarska oznaka, godina prve registracije te cijena u eur.
'''

# vehicle_type => car, truck, motorcycle, bicycle, agriculture, marine
vehicle = {} # prazan set => set(), a prazan rjecnik samo s viticasatim zagradama {}
vehicle_db = []

vehicle_db.append(vehicle) # Dodao sam prazan rjecnik na index 0
#                               kako bih kasnije mogao dohvatiti prvo vozilo s indeksom 1

while True:
    # TODO Ispisite sve tipove vozila tako da ispred svakog navedete redni broj
    #   Trazite korisnika da selektira jedan broj i tako izabere tip vozila
    vehicle['vehicle_type'] = input('Upisite tip vozila: ')
    vehicle['manufacturer'] = input('Upisite proizvodaca vozila: ')
    vehicle['production_year'] = int(input('Upisite godinu proizvodnje vozila: '))
    vehicle['license_plate'] = input('Upisite registarsku oznaku vozila: ')
    vehicle['purchased_price'] = float(input('Upisite nabavnu cijenu vozila: '))

    vehicle_db.append(vehicle)

    next_vehicle = input('Zelite li dodati novo vozilo? (da/ne): ')
    if next_vehicle.lower() != 'da':
        break


print(vehicle_db[1])
