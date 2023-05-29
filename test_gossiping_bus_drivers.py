import unittest
from gossiping_bus_drivers import BusSystem


class TestGossipingBusDrivers(unittest.TestCase):
    #Negativ Test kein Fahrer
    def test_no_drivers(self):
        bus_system = BusSystem([])
        self.assertEqual(bus_system.run(), "never")

    #Negativ Test keine Routen
    def test_no_routes(self):
        bus_system = BusSystem([[], [], []])
        self.assertEqual(bus_system.run(), "never")
    
    # Test mit Routen, die sich nie treffen:
    def test_non_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(bus_system.run(), "never")
    
    # Test mit mehreren Routen, die sich mind. 1x treffen:
    def test_meeting_routes(self):
        bus_system = BusSystem([[1], [1]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Routen unterschiedlicher Längen
    def test_different_length_routes(self):
        bus_system = BusSystem([[1, 2], [1]])
        self.assertEqual(bus_system.run(), 1)

    # Test, ob Gosspis korrekt ausgetauscht werden    
    def test_gossip_exchange(self):
        bus_system = BusSystem([[1, 2], [1]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Routen, die sich erst am Ende des Tages treffen
    def test_end_of_day_meeting_routes(self):
        bus_system = BusSystem([[3, 1, 2, 3], [3, 2, 3, 1], [1, 2, 3]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Routen, die sich nur zu Beginn des Tages treffen
    def test_beginning_of_day_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3], [3, 1, 2], [2, 3, 1]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Routen, die sich zur Mitte des Tages treffen
    def test_middle_of_day_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3], [3, 1]])
        self.assertEqual(bus_system.run(), 3)

    # Test mit sehr vielen Routen
    def test_large_number_of_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4, 5] for _ in range(100)])
        self.assertEqual(bus_system.run(), 1)

    # Test mit sehr vielen Stops
    def test_large_number_of_stops(self):
        bus_system = BusSystem([[i for i in range(1, 1001)]])
        self.assertEqual(bus_system.run(), 1)

    # Test mit Mix verschiedenere Situationen
    def test_mixed_situations(self):
        bus_system = BusSystem([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 7, 8, 9, 10]])
        self.assertEqual(bus_system.run(), 2)

if __name__ == "__main__":
    unittest.main()