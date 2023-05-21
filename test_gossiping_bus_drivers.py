import unittest
from gossiping_bus_drivers import BusSystem

class TestGossipingBusDrivers(unittest.TestCase):
    def test_single_route(self):
        bus_system = BusSystem([[1, 2, 3, 4]])
        self.assertEqual(bus_system.run(), 1)

    def test_never_meeting_routes(self):
        bus_system = BusSystem([[1, 2, 3, 4], [5, 6, 7, 8]])
        self.assertEqual(bus_system.run(), 'never')

    # ...weitere Tests später hinzufügen...
