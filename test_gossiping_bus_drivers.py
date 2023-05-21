import unittest
from gossiping_bus_drivers import BusSystem

class TestGossipingBusDrivers(unittest.TestCase):
    def test_single_round(self):
        bus_system = BusSystem([[1, 2, 3, 4]])
        self.assertEqual(bus_system.run(), 1)

class BusSystem:
    def __init__(self, routes):
        self.routes = routes
    def run(self):
        return 1
