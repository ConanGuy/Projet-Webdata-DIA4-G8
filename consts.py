AGENCY_DICT = None
CALENDAR_DICT = None
FEED_INFO_DICT = None
ROUTE_DICT = None
STOP_TIME_DICT = None
STOP_DICT = None
TRANSFER_DICT = None
TRIP_DICT = None

from rdflib import Graph
import pickle

G_TGVMAX = pickle.load(open('rdf_obj/tgvmax.pkl', 'rb'))
G_GARES = pickle.load(open('rdf_obj/gares-tgv.pkl', 'rb'))
G_USERNAME = pickle.load(open('rdf_obj/username.pkl', 'rb'))
G_TEMP = pickle.load(open('rdf_obj/temperatures.pkl', 'rb'))
