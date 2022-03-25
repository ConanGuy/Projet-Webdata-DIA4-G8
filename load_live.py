import requests
from bs4 import BeautifulSoup
import pandas as pd

def load_live():
    df = pd.DataFrame(columns=["ville", "temp"])

    liste = [ ["https://weather.com/fr-FR/temps/aujour/l/1a8af5b9d8971c46dd5a52547f9221e22cd895d8d8639267a87df614d0912830", "Paris"], ["https://weather.com/fr-FR/temps/aujour/l/a85705fcb91d61ff16c943ea187279dac0446bd8551a41012fc8a84e498f3b4d", "Toulouse"], ["https://weather.com/fr-FR/temps/aujour/l/97adc36f89aa35486ece34380b006f2c946ef82fad53a58954c33e39e23948fe", "Marseille"], ["https://weather.com/fr-FR/temps/aujour/l/7615c204059d6d10382d733bf8dc1718bcac1e82e2f2cf66e6842581ca9360c2", "Lyon",], ["https://weather.com/fr-FR/temps/aujour/l/1974190528350439b654203c5f1019f02bf8447deb66f47462c901dbd8d6775c", "Bordeaux"], ["https://weather.com/fr-FR/temps/aujour/l/7c126606f32c2d6a177f059444d5a299243d497905461a728b91239ec22c23bb", "Nice"], ["https://weather.com/fr-FR/temps/aujour/l/8093222845e3d267100f81d4100a5641d608eb4c14db0e83df2f8b8be0fce76f", "Nantes", "https://weather.com/fr-FR/temps/aujour/l/e83a2bc15fa5503ca0afe77c2121f8cdb6ba19c1b081db84278bfc5e74a78c5e", "Lille"], ["https://weather.com/fr-FR/temps/aujour/l/bc96a77b2944f434fe161ce68d1e37ca36557701b1e558b44934281e1b2c0c48", "Strasbourg"]]
    for element in liste : 
    #Paris
        URL = element[0]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        temp = soup.find_all("span",  class_="CurrentConditions--tempValue--3a50n")
        
        value=str(temp)
        value
        value = value.split('Value">')[1]
        value
        temp= value.split("</")[0]
        df2 = pd.DataFrame([[element[1], temp]], columns=["ville", "temp"])
        df = pd.concat([df,df2])
    df.to_csv("csv/temperatures.csv", index=False)

    from load_rdf import csv_to_rdf

    csv_to_rdf("temperatures", "Temperature")