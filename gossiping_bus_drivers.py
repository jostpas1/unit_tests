class BusSystem:
    def __init__(self, routes):
        self.routes = routes
        self.drivers = {i: set([i]) for i in range(len(routes))}

    def run(self):
        if not self.routes or not any(self.routes):
            return "never"

        for time in range(480):  # 480 minutes in an 8-hour shift
            stops = {i: self.routes[i][time % len(self.routes[i])] for i in range(len(self.routes))}
            gossips = self.drivers.copy()

            for i in stops:
                for j in stops:
                    if i != j and stops[i] == stops[j]:
                        gossips[i] = gossips[i].union(self.drivers[j])
                        gossips[j] = gossips[j].union(self.drivers[i])

            self.drivers = gossips

            if all(len(driver_gossips) == len(self.drivers) for driver_gossips in self.drivers.values()):
                return time + 1  # Return the current minute

        return "never"
