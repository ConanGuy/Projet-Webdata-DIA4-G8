# Web Semantic Project

ESILV - Semantic Web Project - 2022

---

For this Project we used the following categories as databases :
- temperature (real time)
- gares-tgv (static)
- tgvmax (static)
- username (static)

Our project is structured the following way :
- `Projet-Webdata-DIA4-G8/` : Contains our main code, SPARQL queries, the code to load our rdf and dynamic temperature data as well as a txt file for requirements
- `Projet-Webdata-DIA4-G8/gui/` : Where our widget python code is
- `Projet-Webdata-DIA4-G8/json-ld/` : Where all our json files are stored
- `Projet-Webdata-DIA4-G8/csv/` : Containing our data in csv form


## Utilisation

Launch the following command to get all the required dependencies:
`pip install -r requirements.txt`

To generate RDF file, run this command in your terminal:
`python load_rdf.py`

Finally you can run the following command to open the application:
`python main.py`


## Vidéo
[![Watch the video](https://i.imgur.com/vKb2F1B.png)](demo_vid.mp4)