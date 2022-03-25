from rdflib import Graph
import json
import pandas as pd
import pickle

def jsonld_to_rdf(filename):    
    # On ouvre le fichier jsonld
    jsonld_obj = json.load(open("json-ld/"+filename+".json", "r"))
    
    # On créer le graph rdf depuis le jsonld
    g = Graph().parse(data=json.dumps(jsonld_obj), format="json-ld")
    
    # By default serialize to rdf/xml
    rdf_data = g.serialize(destination="rdf/"+filename+".rdf".format(filename), format='pretty-xml')

    # On enregistre l'objet Graph dans un fichier pour pouvoir accélérer l'ouverture du programme principale
    pickle.dump(rdf_data, open("rdf_obj/"+filename+".pkl", "wb"), pickle.HIGHEST_PROTOCOL)

    return rdf_data
    
def csv_to_jsonld(filename, type_name):
    # Ouverture du csv
    df = pd.read_csv("csv/"+filename+".csv", na_values="", encoding="latin1")
    
    # Récupération des colonnes
    columns = df.columns
    
    # Crétaion de la base (@context) du jsonld
    jsonld_obj = {
        "@context": {
            "@vocab": f"http://www.semanticweb.org/ontologies/2022/2/{type_name.lower()}#", # En nom on met le type de l'objet qu'on a envoyé en paramètre
            "@base": f"http://www.semanticweb.org/ontologies/2022/2/{type_name.lower()}",
            "id": "@id",    
        },
        "features": []
    }
    
    # Dans le context on rajoute les variables possibles d'un objet on annonçant sont type (int, string, etc.)
    for column in columns:
        jsonld_obj["@context"][column] = {
            "@id": column, # Nom de la colonne
            "@type": "http://www.w3.org/2001/XMLSchema#string" # string our tous car manque de temps pour gérer la détection
        }
    
    # On parcours les lignes du csv
    for index, row in df.iterrows():
        
        # On créer le json pour la ligne
        obj = {
            "type": type_name,
            "properties": {}
        }
        
        # On rajoute une porperty par colonne avec sa valeur
        for column in columns:
            obj["properties"][column] = str(row[column]) if str(row[column]) != "nan" else ""
        
        # On ajoute l'objet aux features du jsonld
        jsonld_obj["features"].append(obj)

    # On enregistre le jsonld dans un fichier .json
    json.dump(jsonld_obj, open("json-ld/"+filename+".json", "w"))

def csv_to_rdf(filename, type_name):
    csv_to_jsonld(filename, type_name)
    jsonld_to_rdf(filename)
    
if __name__ == "__main__":
    import load_live
    load_live.load_live()
    csv_to_rdf("gares_tgv", "GareTGV")
    csv_to_rdf("tgvmax", "TGVMax")
    csv_to_rdf("username", "Username")