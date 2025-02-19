'''
Kreirajte bazu s vozilima firme.
ID svakog retka je cijeli broj,
a podaci koji se čuvaju o svakom vozilu su:
tip, proizvođač, registarska oznaka, godina prve registracije te cijena u eur.
'''

vehicle_type = '' # car, truck, motorcycle, bicycle, agriculture, marine
manufacturer = ''
production_year = 1990
license_plate = ''
purchased_price = 0.0

vehicle_db = []

while True:
    # TODO Ispisite sve tipove vozila tako da ispred svakog navedete redni broj
    #   Trazite korisnika da selektira jedan broj i tako izabere tip vozila
    vehicle_type = input('Upisite tip vozila: ')
    manufacturer = input('Upisite proizvodaca vozila: ')
    production_year = int(input('Upisite godinu proizvodnje vozila: '))
    license_plate = input('Upisite registarsku oznaku vozila: ')
    purchased_price = float(input('Upisite nabavnu cijenu vozila: '))


    next_vehicle = input('Zelite li dodati novo vozilo? (da/ne): ')
    if next_vehicle.lower() != 'da':
        break
