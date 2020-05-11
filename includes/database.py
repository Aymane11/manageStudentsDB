# Import sqlite lib
import sqlite3 as sql
from sqlite3 import Error

# Include helpers
from includes.helper import *

# Configuration
config = {
    "database": DATABASE_PATH + "/database.sqlite",
}

# Try to connect to our sqlite db :)
try:
    db = sql.connect(config['database'])
except Error:
    exit("An error occured while trying to connect to DB !")

# Tables
tables = {

    # Table Auteur
    "Auteur": {
        'foreignKeys': {

        },
        'primaryKeys': [
            'NAuteur'
        ],
        'attributes': {
            'NAuteur': 		['INTEGER'],
            'nomA': 		['VARCHAR(50)', 'NOT NULL'],
            'prenomA': 		['VARCHAR(50)', 'NOT NULL'],
            'nationalite': ['VARCHAR(50)', 'NOT NULL']
        }
    },

    # Table Livre
    "Livre": {
        'foreignKeys': {

        },
        'primaryKeys': [
            'Nlivre'
        ],
        'attributes': {
            'Nlivre': 	['INTEGER'],
            'num_ISBN': ['VARCHAR(17)', 'NOT NULL'],
            'titre': 	['VARCHAR(50)', 'NOT NULL'],
            'nbPages': 	['INTEGER', 'NOT NULL'],
            'anneeS': 	['VARCHAR(4)', 'NOT NULL'],
            'prix': 	['REAL', 'NOT NULL']
        }
    },

    # Table Possede
    "Possede": {
        'foreignKeys': {
            'Nlivre': 'Livre',
            'Nauteur': 'Auteur'
        },
        'primaryKeys': [
        ],
        'attributes': {
            'Nlivre': 	['INTEGER', 'NOT NULL'],
            'Nauteur': 	['INTEGER', 'NOT NULL']
        }
    },

    # Table Classe
    "Classe": {
        'foreignKeys': {

        },
        'primaryKeys': [
            'numClasse'
        ],
        'attributes': {
            'numClasse': ['INTEGER', 'NOT NULL'],
            'nomClasse': ['VARCHAR(50)', 'NOT NULL'],
        }
    },

    # Table Etudiant
    "Etudiant": {
        'foreignKeys': {
            'numClasse': 'Classe'
        },
        'primaryKeys': [
            'num_etu'
        ],
        'attributes': {
            'num_etu': 			['INTEGER', 'NOT NULL'],
            'nomE': 			['VARCHAR(50)', 'NOT NULL'],
            'prenomE': 			['VARCHAR(50)', 'NOT NULL'],
            'date_naissance': 	['VARCHAR(50)', 'NOT NULL'],
            'ville': 			['VARCHAR(50)', 'NOT NULL'],
            'dateInscripBU': 	['VARCHAR(50)', 'NOT NULL'],
            'dateAbs': 			['VARCHAR(50)'],
            'numClasse': 		['INTEGER', 'NOT NULL']
        }
    },

    # Table Inscrit
    "Inscrit": {
        'foreignKeys': {
            'num_etu':		'Etudiant',
                        'num_cours': 	'Cours'},
        'primaryKeys': [
        ],
        'attributes': {
            'num_etu': 		['INTEGER', 'NOT NULL'],
            'num_cours': 	['INTEGER', 'NOT NULL'],
            'dateInsc': 	['VARCHAR(50)', 'NOT NULL']
        }
    },

    # Table Pret
    "Pret": {
        'foreignKeys': {
            'num_etu': 'Etudiant',
            'Nlivre': 'Livre'
        },
        'primaryKeys': [
            'Npret'
        ],
        'attributes': {
            'Npret': 			['INTEGER', 'NOT NULL'],
            'num_etu': 			['INTEGER', 'NOT NULL'],
            'Nlivre': 			['INTEGER', 'NOT NULL'],
            'datePret': 		['VARCHAR(50)', 'NOT NULL'],
            'dateRetour': 		['VARCHAR(50)'],
            'DateRetourPrevue': ['VARCHAR(50)']
        }
    },

    # Table Enseignant
    "Enseignant": {
        'foreignKeys': {

        },
        'primaryKeys': [
            'num_ens'
        ],
        'attributes': {
            'num_ens': 		['INTEGER', 'NOT NULL'],
            'nomP': 		['VARCHAR(50)', 'NOT NULL'],
            'prenomP': 		['VARCHAR(50)', 'NOT NULL'],
            'specialite': 	['VARCHAR(50)', 'NOT NULL'],
            'departement': 	['VARCHAR(50)', 'NOT NULL']
        }
    },

    # Table Cours
    "Cours": {
        'foreignKeys': {
            'num_ens': 'Enseignant'
        },
        'primaryKeys': [
            'num_cours'
        ],
        'attributes': {
            'num_cours': 	['INTEGER', 'NOT NULL'],
            'nomC': 		['VARCHAR(50)', 'NOT NULL'],
            'nb_heures': 	['INTEGER', 'NOT NULL'],
            'num_ens':		['INTEGER', 'NOT NULL']
        }
    },

    # Table Resultat
    "Resultat": {
        'foreignKeys': {
            'num_etu':		'Etudiant',
                        'num_cours': 	'Cours'
        },
        'primaryKeys': [
        ],
        'attributes': {
            'num_etu': 		['INTEGER', 'NOT NULL'],
            'num_cours': 	['INTEGER', 'NOT NULL'],
            'note': 		['REAL', 'NOT NULL']
        }
    },

    # Table Charge
    "Charge": {
        'foreignKeys': {
            'num_ens': 'Enseignant',
            'num_cours': 'Cours',
        },
        'primaryKeys': [
        ],
        'attributes': {
            'num_cours': 	['INTEGER', 'NOT NULL'],
            'num_ens': 		['INTEGER', 'NOT NULL'],
            'nbH': 			['INTEGER', 'NOT NULL']
        }
    },

}