import consts

class Stop:
    
    def __init__(self, stop_id, stop_name, stop_desc, stop_lat, stop_lon, zone_id, stop_url, location_type, parent_station):
        self.id = stop_id
        self.stop_name = stop_name
        self.stop_desc = stop_desc
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
        self.zone_id = zone_id
        self.stop_url = stop_url
        self.location_type = location_type
        self.parent_station = parent_station
        
    def __str__(self):
        return self.id
        
    def load(file="export-ter-gtfs-last/stops.csv"):        
        if consts.STOP_DICT is not None:
            return consts.STOP_DICT
        
        import csv
        
        consts.STOP_DICT = {}
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                obj = Stop(*row)
                consts.STOP_DICT[obj.id] = obj
                
        return consts.STOP_DICT

if __name__ == "__main__":
    d = Stop.load()
    
    print(d[list(d.keys())[0]])
