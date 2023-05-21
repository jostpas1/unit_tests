import unittest
from gossiping_bus_drivers import BusSystem

class TestGossipingBusDrivers(unittest.TestCase):
    
    # Test mit nur einer Route:    
    def test_single_route(self):
        bus_system = BusSystem([[1, 2, 3, 4]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Routen, die sich nie treffen:
    def test_never_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4], [5, 6, 7, 8]])
        self.assertEqual(bus_system.run(), 'never')

    # Test mit mehreren Routen, die sich mind. 1x treffen:
    def test_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4], [4, 5, 6, 7]])
        self.assertEqual(bus_system.run(), 4)

    # Test, ob Gosspis korrekt ausgetauscht werden
    def test_gossip_exchange(self):
        bus_system = BusSystem([[1, 2, 3, 4], [4, 5, 6, 7]])
        self.assertEqual(bus_system.get_all_gossips(), {1: {1, 2}, 2: {1, 2}})

    # Test mit Routen unterschiedlicher Längen
    def test_different_length_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4], [3, 4]])
        self.assertEqual(bus_system.run(), 3)

    # Test mit Routen, die sich erst am Ende des Tages treffen
    def test_end_of_day_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4, 5], [5]])
        self.assertEqual(bus_system.run(), 5)

    # Test mit Routen, die sich nur zu Beginn des Tages treffen
    def test_beginning_of_day_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4], [1, 6, 7, 8]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Routen, die sich zur Mitte des Tages treffen
    def test_middle_of_day_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4], [3]])
        self.assertEqual(bus_system.run(), 3)

    # Test mit sehr vielen Routen
    def test_large_number_of_routes(self):
        bus_system = BusSystem([[i, i + 1, i + 2, i + 3] for i in range(1000)])
        self.assertEqual(bus_system.run(), 'never')

    # Test mit sehr vielen Haltestellen
    def test_large_number_of_stops(self):
        bus_system = BusSystem([[i for i in range(1000)], [999]])
        self.assertEqual(bus_system.run(), 1000)

    # Test mit Mix verschiedenere Situationen
    def test_mixed_situations(self):
        bus_system = BusSystem([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                                [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
                                [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]])
        self.assertEqual(bus_system.run(), 'never')