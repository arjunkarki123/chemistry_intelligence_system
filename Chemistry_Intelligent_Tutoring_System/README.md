# chemistry_intelligence_system
Chemistry Intelligent Tutoring System

This project is a Chemistry Intelligent Tutoring System that uses Flask as a web framework and RDFlib for semantic data processing. The system parses an RDF ontology file to extract and display hierarchical relationships between chemistry concepts, such as classes and their subclasses.

Features:
Ontology Parsing: Utilizes the RDFlib library to parse an RDF file (Chemistry ontology.rdf) containing chemistry-related concepts.

SPARQL Queries: Extracts class and parent-child relationships from the ontology using SPARQL.

Hierarchical Representation: Organizes and displays the ontology structure in a user-friendly, hierarchical format.

Web Interface: Built with Flask to serve the ontology data on a web page.
Project Structure

app.py: Main application file that integrates Flask and RDFlib to process and serve ontology data.

Chemistry ontology.rdf: RDF file containing the chemistry ontology. Replace this with your actual ontology file.

templates/index.html: HTML template to render the hierarchical structure of the ontology.
static/: (Optional) Directory for static assets like CSS, JavaScript, or images.

Installation:

Clone the repository:
git clone https://github.com/<your-username>/chemistry_intelligence_system.git
cd chemistry_intelligence_system

Install the required dependencies:
pip install flask rdflib

Usage:
Run the application:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000/

