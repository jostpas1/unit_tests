class BusSystem:
    def __init__(self, routes):
        self.routes = routes
        self.gossips = [set([i]) for i in range(len(routes))]

    def all_gossips_exchanged(self):
        all_gossips = set(range(len(self.routes)))
        return all(self.gossips[driver] == all_gossips for driver in self.gossips)

    def run(self):
        for time in range(480):
            stops = [route[time % len(route)] for route in self.routes]
            for i in range(len(stops)):
                for j in range(i + 1, len(stops)):
                    if stops[i] == stops[j]:
                        self.gossips[i].update(self.gossips[j])
                        self.gossips[j].update(self.gossips[i])
            if self.all_gossips_exchanged():
                return time + 1
        return 'never'