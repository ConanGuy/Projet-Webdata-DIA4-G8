import consts

class Calendar:
    
    def __init__(self, service_id, date, exception_type):
        self.id = service_id
        self.agency_name = date
        self.agency_url = exception_type
        
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.__str__()
        
    def load(file="export-ter-gtfs-last/calendar_dates.csv"):
        if consts.CALENDAR_DICT is not None:
            return consts.CALENDAR_DICT
        
        import csv
        
        consts.CALENDAR_DICT = {}        
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                agency = Calendar(*row)
                consts.CALENDAR_DICT[agency.id] = agency
                
        return consts.CALENDAR_DICT

if __name__ == "__main__":
    print(Calendar.load())
