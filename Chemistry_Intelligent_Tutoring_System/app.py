from flask import Flask, render_template
import rdflib

# Initialize Flask app
app = Flask(__name__)

# Load RDF data using RDFlib
g = rdflib.Graph()

# Load your RDF file (replace this with the correct file path)
g.parse("Chemistry ontology.rdf", format="xml")

# SPARQL query to extract classes and individuals, grouping them by parent-child relationships
query = """
    SELECT ?class ?parent ?label
    WHERE {
        ?class rdfs:subClassOf ?parent .
        OPTIONAL {
            ?class rdfs:label ?label .
        }
    }
"""
results = g.query(query)

# Organizing the classes in a hierarchical structure
ontology_structure = {}

# Processing the results into a hierarchical dictionary
for row in results:
    rdf_class = str(row[0])
    parent_class = str(row[1])
    label = str(row[2]) if row[2] else rdf_class.split("#")[-1]

    if parent_class not in ontology_structure:
        ontology_structure[parent_class] = []

    ontology_structure[parent_class].append({
        'class': rdf_class,
        'label': label
    })

@app.route('/')
def index():
    return render_template('index.html', ontology_structure=ontology_structure)

if __name__ == '__main__':
    app.run(debug=True)
