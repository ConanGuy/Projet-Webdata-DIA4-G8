import consts
from Stop import Stop
from Route import Route

routeDic = Stop.load()

class Transfer:
    
    def __init__(self, from_stop_id, to_stop_id, transfer_type, min_transfer_time, from_route_id, to_route_id):
        self.id = from_stop_id+" - "+to_stop_id
        self.from_stop_id = Stop[from_stop_id]
        self.to_stop_id = Stop[to_stop_id]
        self.transfer_type = transfer_type
        self.min_transfer_time = min_transfer_time
        self.min_transfer_time = min_transfer_time
        self.from_route_id = Route[from_route_id]
        self.to_route_id = Route[to_route_id]
        
    def __str__(self):
        return self.id
        
    def load(file="export-ter-gtfs-last/transfers.csv"):
        if consts.TRANSFER_DICT is not None:
            return consts.TRANSFER_DICT
        
        import csv
        
        consts.TRANSFER_DICT = {}
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                obj = Transfer(*row)
                consts.TRANSFER_DICT[obj.id] = obj
                
        return consts.TRANSFER_DICT

if __name__ == "__main__":
    Transfer.load()
