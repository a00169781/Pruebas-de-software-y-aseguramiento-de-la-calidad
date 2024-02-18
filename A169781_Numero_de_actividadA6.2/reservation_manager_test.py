""" Script de pruebas para validar las clases Hotel, Reservation y Customer"""
import unittest
import os
from reservation_manager import carga_json, guarda_json
from reservation_manager import Hotel, Customer, Reservation


class TestHelperFunctions(unittest.TestCase):
    """ Clase de prueba para las funciones que
    están fuera de las clases de objetos """
    def test_carga_json_hotel(self):
        """ Prueba para cargar un archivo json tipo Hotel """
        _json = carga_json('hotel')
        self.assertIs(type(_json), dict)

    def test_carga_json_customer(self):
        """ Prueba para cargar un archivo json tipo Customer """
        _json = carga_json('customer')
        self.assertIs(type(_json), list)

    def test_carga_json_reservation(self):
        """ Prueba para cargar un archivo json tipo Reservation """
        _json = carga_json('reservation')
        self.assertIs(type(_json), dict)

    def test_carga_json_exception(self):
        """ Prueba Negativa, esta valida que solo podamos cargar los
        archivos de tipo hotel, customer o reservation si intentamos
        cargar otro tipo de archivo regresa una excepción """
        self.assertRaises(ValueError, carga_json, 'hostel')

    def test_guarda_json_exception(self):
        """ Prueba Negativa, esta valida que solo podamos guardar los
        archivos de tipo hotel, customer o reservation si intentamos
        cargar otro tipo de archivo regresa una excepción """
        self.assertRaises(ValueError, guarda_json, 'hostel', {})


class TestHotel(unittest.TestCase):
    """ Rutinas para validar la clase Hotel """
    def setUp(self):
        self.hotel = Hotel('Mi Hotel de Prueba')

    def test_hotel_is_created_in_file(self):
        """ Test para validar la serialización y guardado en
        disco de los objetos Hotel """
        hotel_json = carga_json('hotel')
        self.assertTrue(self.hotel.name in hotel_json)

    def test_hotel_saved_to_disk(self):
        """ Test para validar guardado en disco de los objetos Hotel """
        new_hotel = Hotel('Nuevo Hotel de Prueba')
        new_hotel.save_to_disk()
        hotel_json = carga_json('hotel')
        self.assertTrue('Nuevo Hotel de Prueba' in hotel_json)

    def test_create_hotel(self):
        """ Test para validar la creación de un objeto Hotel """
        self.hotel = Hotel('Nuevo Hotel')
        with self.subTest():
            self.assertEqual('Nuevo Hotel', self.hotel.name)
        with self.subTest():
            self.assertFalse(self.hotel.reservado)

    def test_delete_hotel(self):
        """ Test para validar el método delete_hotel """
        name = self.hotel.name
        self.hotel.delete_hotel(name)
        hotel_json = carga_json('hotel')
        self.assertFalse(name in hotel_json)

    def test_delete_hotel_exeption(self):
        """ Prueba Negativa, valida que no se puedan borrar
        hoteles que no existen """
        name = "Mi hotel que no existe"
        self.assertRaises(ValueError, self.hotel.delete_hotel, name)

    def test_modify_hotel(self):
        """ Test para validar el método modify_info de la clase Hotel """
        old_name = self.hotel.name
        self.hotel.modify_info(old_name + 'Modificado')
        self.assertEqual(old_name + 'Modificado', self.hotel.name)

    def test_hotel_reserve(self):
        """ Test para validar el método reserve de la calse hotel """
        self.hotel.reserve()
        self.assertTrue(self.hotel.reservado)

    def test_hotel_reserve_exeption(self):
        """ Prueba Negativa Test que no se puede reservar un hotel lleno """
        self.assertRaises(ValueError, self.hotel.reserve, )

    def test_hotel_cancel_reservation(self):
        """ Test para validar el método cancel_reservation """
        self.hotel.reserve()
        self.hotel.cancel_reservation()
        self.assertFalse(self.hotel.reservado)

    def test_hotel_cancel_reservation_exception(self):
        """ Prueba Negativa Test para validar el método cancel_reservation """
        self.assertRaises(ValueError, self.hotel.cancel_reservation, )


class TestCustomer(unittest.TestCase):
    """ Rutinas para validar la clase Customer """
    def setUp(self):
        self.customer = Customer('Joe Doe')

    def test_hotel_saved_to_disk(self):
        """ Test para validar que los datos se serialicen y
         se guarden en un archivo """
        new_customer = Customer('Jane Doe')
        new_customer.save_to_disk()
        customer_json = carga_json('customer')
        self.assertTrue('Jane Doe' in customer_json)

    def test_create_customer(self):
        """ Test para validar la creación de un cliente """
        self.customer = Customer('Joe Jane Doe')
        self.assertEqual('Joe Jane Doe', self.customer.name)

    def test_detlete_customer_exeption(self):
        """ Test para validar la remoción de un cliente """
        name = self.customer.name + ' No existe'
        self.assertRaises(ValueError, self.customer.delete_customer, name)

    def test_detlete_customer(self):
        """ Test para validar la remoción de un cliente """
        name = self.customer.name
        self.customer.delete_customer(name)
        _json = carga_json('customer')
        self.assertFalse(name in _json)

    def test_modify_customer_info(self):
        """ Test para validar el método modify_info de un cliente """
        old_name = self.customer.name
        self.customer.modify_info(old_name + 'Modificado')
        self.assertEqual(old_name + 'Modificado', self.customer.name)


class TestReservation(unittest.TestCase):
    """ Rutinas para validad la clase Reservación """
    def test_reservation_save_to_disk(self):
        """ Test para validar que los datos se serialicen
         y se guarden en un arachivo """
        hotel = Hotel('test_reservation_save_to_disk')
        customer = Customer('test_reservation_save_to_disk')
        reservation = Reservation(customer, hotel)
        _json = carga_json('reservation')
        self.assertTrue(reservation.hotel in _json)

    def test_cancel_reservation(self):
        """ Test para validar la cancelación de una reservación """
        hotel = Hotel('test_cancel_reservation Hotel')
        customer = Customer('test_cancel_reservation Customer')
        reservation = Reservation(customer, hotel)
        reservation.cancel_reservation()
        hotel = Hotel('test_cancel_reservation Hotel')
        self.assertFalse(hotel.reservado)


if __name__ == '__main__':
    for file_name in ['hotel.json', 'customer.json', 'reservation.json']:
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('File not found: ' + file_name)
    unittest.main()
