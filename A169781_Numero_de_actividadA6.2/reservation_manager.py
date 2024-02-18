"""Este modulo implementa
Clases muy básicas para probar pruebas unitarias"""

import json
import os

SUPORTED_TYPES = ['hotel', 'reservation', 'customer']


def carga_json(tipo):
    """Función para cargar archivos de json"""
    if tipo not in SUPORTED_TYPES:
        raise ValueError("""Solo se pueden cargar archivos
         para 'hotel', 'reservation', 'customer'""")
    file_name = tipo + ".json"
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as outfile:
            if tipo == 'customer':
                json.dump([], outfile)
            else:
                json.dump({}, outfile)

    with open(file_name, 'r', encoding="utf-8") as _json_file:
        _json_blob = json.load(_json_file)
    return _json_blob


def guarda_json(tipo, json_blob):
    """Función para salvar archivos de json"""
    if tipo not in SUPORTED_TYPES:
        raise ValueError("""Solo se pueden cargar
         archivos para " + SUPORTED_TYPES""")
    with open(tipo + ".json", 'w', encoding="utf-8") as _json_file:
        json.dump(json_blob, _json_file)
    return 0


class Hotel:
    """Clase que representa a un Hotel
    Por simplicidad todos los hoteles tiene unicamente
    1 cuarto"""

    def __init__(self, name):
        """Metodo para instansear un objeto Hotel
        cada vez que creamos hotel buscamos si ya existe en el archivo
        json, si no existe creamos uno nuevo si existe cargamos
        su estatus de reservacion"""
        hotel_blob = carga_json('hotel')
        reservado = False
        if name in hotel_blob:
            reservado = hotel_blob[name]
        self.name = name
        self.reservado = reservado
        self.save_to_disk()

    def save_to_disk(self):
        """ Guarda datos a disco """
        hotel_blob = carga_json('hotel')
        hotel_blob[self.name] = self.reservado
        guarda_json('hotel', hotel_blob)

    @staticmethod
    def create_hotel(name):
        """Crea un hotel nuevo, el hotel se crea con disponibilidad
        si el hotel ya existia carga los datos existentes"""
        return Hotel(name)

    @staticmethod
    def delete_hotel(name):
        """ Borra hotel """
        hotel_blob = carga_json('hotel')
        if name not in hotel_blob:
            raise ValueError('Hotel: ' + name + ' not found')
        del hotel_blob[name]
        guarda_json('hotel', hotel_blob)

    def desplay_info(self):
        """ Imprime la información del Hotel """
        print('nombre: ' + self.name + ' reservado:' + self.reservado)

    def modify_info(self, new_name):
        """ Modifica la información del hotel """
        self.name = new_name
        self.save_to_disk()

    def reserve(self):
        """ Reserva el único cuarto que tiene el hotel """
        if self.reservado:
            raise ValueError('Cannot reserve, hotel already fully booked')
        self.reservado = True
        self.save_to_disk()

    def cancel_reservation(self):
        """ Cancela la reservación """
        if not self.reservado:
            raise ValueError('No reservation for this hotel, cannot cancel')
        self.reservado = False
        self.save_to_disk()


class Customer:
    """Clase que representa a un Customer
    para practicar pruebas unitarias"""

    def __init__(self, name):
        """Metodo para instansear un objeto Customer, por simplicidad
        el Customer solo tiene un nombre como dato"""
        self.name = name
        self.save_to_disk()

    def save_to_disk(self):
        """ Guarda datos a disco """
        customer_blob = carga_json('customer')
        if self.name not in customer_blob:
            customer_blob.append(self.name)
        guarda_json('customer', customer_blob)

    @staticmethod
    def create_customer(name):
        """Crea un hotel nuevo, el hotel se crea con disponibilidad
        si el hotel ya existia carga los datos existentes"""
        return Customer(name)

    @staticmethod
    def delete_customer(name):
        """ Borra un Customer """
        customer_blob = carga_json('customer')
        if name not in customer_blob:
            raise ValueError('Hotel: ' + name + ' not found')
        customer_blob.remove(name)
        guarda_json('customer', customer_blob)

    def desplay_info(self):
        """ Imprime la información del Customer """
        print('nombre: ' + self.name)

    def modify_info(self, new_name):
        """ Modifica la información del Customer """
        self.delete_customer(self.name)
        self.name = new_name
        self.save_to_disk()


class Reservation:
    """Clase que representa a una Reservación
    para practicar pruebas unitarias"""

    def __init__(self, customer, hotel):
        """Metodo para instansear un objeto Customer, por simplicidad
        el Customer solo tiene un nombre como dato"""
        if hotel.reservado:
            raise ValueError('Hotel: ' + hotel.name +
                             ' no tiene disponibilidad')
        hotel.reserve()
        self.customer = customer.name
        self.hotel = hotel.name
        self.save_to_disk()

    def save_to_disk(self):
        """ Guarda datos a disco """
        reservation_blob = carga_json('reservation')
        reservation_blob[self.hotel] = self.customer
        guarda_json('reservation', reservation_blob)

    def cancel_reservation(self):
        """ Cancela una reservacion """
        reservation_blob = carga_json('reservation')
        if self.hotel not in reservation_blob:
            raise ValueError('Hotel: ' + self.hotel +
                  ' not found in reservation records, no need to cancel.')
        hotel = Hotel(self.hotel)
        hotel.cancel_reservation()
        del reservation_blob[self.hotel]
        guarda_json('reservation', reservation_blob)


def main():
    """ Main funtions """
    print("ejecute reservation_manager_test.py para validar el funcionamiento")


if __name__ == '__main__':
    main()
