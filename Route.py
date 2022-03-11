import consts
from Agency import Agency

agencyDic = Agency.load()

class Route:
    
    def __init__(self, route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_urlroute_url, route_color,route_text_color):
        self.route_id = route_id
        self.agency_id = agency_id
        self.trroute_short_namep_id = route_short_name
        self.route_long_name = route_long_name
        self.route_desc = route_desc
        self.route_type = route_type
        self.route_urlroute_url = route_urlroute_url
        self.route_color = route_color
        self.route_text_color = route_text_color
        
    def __str__(self):
        return self.route_id
        
    def load(file="export-ter-gtfs-last/routes.csv"):
        if consts.ROUTE_DICT == {}:
            return consts.ROUTE_DICT
        
        import csv
        
        consts.ROUTE_DICT = {}
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                obj = Route(*row)
                consts.ROUTE_DICT[obj.route_id] = obj
                
        return consts.ROUTE_DICT

if __name__ == "__main__":
    Route.load()
