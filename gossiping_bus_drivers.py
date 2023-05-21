class BusSystem:
    def __init__(self, routes):
        self.routes = routes
        self.gossips = {i: {i} for i in range(len(routes))}

    def run(self):
        for time in range(480):  # Für jede Minute des Tages...
            stops = [route[time % len(route)] for route in self.routes]
            for i, stop in enumerate(stops):
                for j, other_stop in enumerate(stops):
                    if stop == other_stop:
                        self.gossips[i] = self.gossips[i].union(self.gossips[j])
            if len(set(stops)) < len(stops):  # Wenn es eine doppelte Haltestelle gibt, treffen sich die Busse
                return time + 1
        return 'never'

    def get_all_gossips(self):
        return self.gossips
