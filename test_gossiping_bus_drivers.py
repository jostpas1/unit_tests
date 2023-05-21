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

    # ...weitere Tests später hinzufügen...