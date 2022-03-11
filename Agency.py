import consts

class Agency:
    
    def __init__(self, agency_id, agency_name, agency_url, agency_timezone, agency_lang):
        self.id = agency_id
        self.agency_name = agency_name
        self.agency_url = agency_url
        self.agency_timezone = agency_timezone
        self.agency_lang = agency_lang
        
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.__str__()
        
    def load(file="export-ter-gtfs-last/agency.csv"):
        if consts.AGENCY_DICT is not None:
            return consts.AGENCY_DICT
        
        import csv
        
        consts.AGENCY_DICT = {}        
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                agency = Agency(*row)
                consts.AGENCY_DICT[agency.id] = agency
                
        return consts.AGENCY_DICT

if __name__ == "__main__":
    print(Agency.load())
