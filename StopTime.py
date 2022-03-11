import consts
from Stop import Stop
from Trip import Trip

stopDic = Stop.load()
tripDic = Trip.load()

class StopTime:
    
    def __init__(self, trip_id, arrival_time, departure_time, stop_id, stop_sequence, stop_headsign, pickup_type, drop_off_type, shape_dist_traveled):
        self.trip = tripDic[trip_id]
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.stop = stopDic[stop_id]
        self.stop_sequence = stop_sequence
        self.stop_headsign = stop_headsign
        self.pickup_type = pickup_type
        self.drop_off_type = drop_off_type
        self.shape_dist_traveled = shape_dist_traveled
        
        self.id = trip_id+" - "+stop_id+": "+departure_time+" - "+arrival_time
                
    def __str__(self):
        return self.id
        
    def load(file="export-ter-gtfs-last/stop_times.csv"):        
        if consts.STOP_TIME_DICT is not None:
            return consts.STOP_TIME_DICT
        
        import csv
        
        consts.STOP_TIME_DICT = {}
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                obj = StopTime(*row)
                consts.STOP_TIME_DICT[obj.id] = obj
                
        return consts.STOP_TIME_DICT

if __name__ == "__main__":
    d = StopTime.load()
    
    print(d[list(d.keys())[0]])
