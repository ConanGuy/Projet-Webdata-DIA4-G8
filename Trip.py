import consts
from Route import Route

routeDic = Route.load()

class Trip:
    
    def __init__(self, route_id, service_id, trip_id, trip_headsign, direction_id, block_id, shape_id):
        self.id = trip_id
        self.route_id = routeDic[route_id]
        self.service_id = service_id
        self.trip_headsign = trip_headsign
        self.direction_id = direction_id
        self.block_id = block_id
        self.shape_id = shape_id
        
    def __str__(self):
        return self.id
        
    def load(file="export-ter-gtfs-last/trips.csv"):
        if consts.TRIP_DICT == {}:
            return consts.TRIP_DICT
        
        import csv
        
        consts.TRIP_DICT = {}        
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                obj = Trip(*row)
                consts.TRIP_DICT[obj.id] = obj
                
        return consts.TRIP_DICT

if __name__ == "__main__":
    Trip.load()
