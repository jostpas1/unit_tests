class BusSystem:
    def __init__(self, routes):
        self.routes = routes

    def run(self):
        # Hinzufügen einer Überprüfung, ob sich die Routen treffen
        for time in range(480):  # Für jede Minute des Tages...
            stops = [route[time % len(route)] for route in self.routes]
            if len(set(stops)) == len(stops):  # Wenn alle Haltestellen einzigartig sind, treffen sich die Busse nie
                return 'never'
        return 1
