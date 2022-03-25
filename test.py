
from rdflib import Graph
import pickle

G_GARES = pickle.load(open('rdf_obj/gares-tgv.pkl', 'rb'))

G_GARES.update("""
INSERT {
	?s a dbonto: POI
}
WHERE {
 ?s a foaf: gare_id
}
"""
)

print(f"After the UPDATE, there are {len(G_GARES)} triples in the graph")