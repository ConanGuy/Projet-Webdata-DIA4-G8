import consts

class FeedInfo:
    
    def __init__(self, feed_id, feed_publisher_name, feed_publisher_url, feed_lang, feed_start_date, feed_end_date, feed_version, conv_rev, plan_rev):
        self.id = feed_id
        self.feed_publisher_name = feed_publisher_name
        self.feed_publisher_url = feed_publisher_url
        self.feed_lang = feed_lang
        self.feed_start_date = feed_start_date
        self.feed_end_date = feed_end_date
        self.feed_version = feed_version
        self.conv_rev = conv_rev
        self.plan_rev = plan_rev
        
    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.__str__()
        
    def load(file="export-ter-gtfs-last/feed_info.csv"):
        if consts.FEED_INFO_DICT is not None:
            return consts.FEED_INFO_DICT
        
        import csv
        
        consts.FEED_INFO_DICT = {}        
        with open(file, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the headers
            for row in reader:
                feedInfo = FeedInfo(*row)
                consts.FEED_INFO_DICT[feedInfo.id] = feedInfo
                
        return consts.FEED_INFO_DICT

if __name__ == "__main__":
    print(FeedInfo.load())
