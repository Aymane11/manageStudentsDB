from inc.DB import *


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
            'nomA': 		['TEXT', 'NOT NULL'],
            'prenomA': 		['TEXT', 'NOT NULL'],
            'nationaliteA': ['TEXT', 'NOT NULL']
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
            'num_ISBN': ['TEXT', 'NOT NULL'],
            'titre': 	['TEXT', 'NOT NULL'],
            'nbPages': 	['INTEGER', 'NOT NULL'],
            'anneeS': 	['TEXT', 'NOT NULL'],
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
			'Nlivre',
			'Nauteur'
        ],
        'attributes': {
            'Nlivre': 	['INTEGER', 'NOT NULL'],
            'Nauteur': 	['INTEGER', 'NOT NULL']
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
            'datePret': 		['TEXT', 'NOT NULL'],
            'dateRetour': 		['TEXT'],
            'DateRetourPrevue': ['TEXT']
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
            'nomE': 			['TEXT', 'NOT NULL'],
            'prenomE': 			['TEXT', 'NOT NULL'],
            'date_naissance': 	['TEXT', 'NOT NULL'],
            'ville': 			['TEXT', 'NOT NULL'],
            'dateInscripBU': 	['TEXT', 'NOT NULL'],
            'dateAbs': 			['TEXT'],
            'numClasse': 		['INTEGER', 'NOT NULL']
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
            'nomClasse': ['TEXT', 'NOT NULL'],
        }
    },

	# Table Cours
    "Cours": {
        'foreignKeys': {
			'num_ens' : 'Enseignant'
        },
        'primaryKeys': [
            'num_cours'
        ],
        'attributes': {
            'num_cours': 	['INTEGER', 'NOT NULL'],
            'nomC': 		['TEXT', 'NOT NULL'],
			'nb_heures': 	['INTEGER', 'NOT NULL'],
			'num_ens':		['INTEGER', 'NOT NULL']
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
            'nomP': 		['TEXT', 'NOT NULL'],
			'prenomP': 		['TEXT', 'NOT NULL'],
			'specialite': 	['TEXT', 'NOT NULL'],
			'departement': 	['TEXT', 'NOT NULL']
        }
    },

	# Table Resultat
    "Resultat": {
        'foreignKeys': {
			'num_etu':		'Etudiant',
			'num_cours' : 	'Cours'
        },
        'primaryKeys': [
			'num_etu',
			'num_cours'
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
			'num_ens' : 'Enseignant'
        },
        'primaryKeys': [
            'num_cours'
        ],
        'attributes': {
            'num_cours': 	['INTEGER', 'NOT NULL'],
            'num_ens': 		['INTEGER', 'NOT NULL'],
			'nbH': 			['INTEGER', 'NOT NULL']
        }
    },

	# Table Inscrit
    "Inscrit": {
        'foreignKeys': {
			'num_etu':		'Etudiant',
			'num_cours' : 	'Cours'        },
        'primaryKeys': [
			'num_etu',
			'num_cours'
		],
        'attributes': {
            'num_etu': 		['INTEGER', 'NOT NULL'],
            'num_cours': 	['INTEGER', 'NOT NULL'],
			'dateInsc': 	['TEXT', 'NOT NULL']
        }
    },

}

cur = db.cursor()


QUERY = ""
queries = []

for nameTable, table in tables.items():
    QUERY += "CREATE TABLE IF NOT EXISTS " + nameTable + " ("
    for attribute in table['attributes']:
        QUERY += attribute + " "
        for typeA in table['attributes'][attribute]:
            QUERY += typeA + " "
        if (attribute in table['primaryKeys']):
            QUERY += "PRIMARY KEY"
        QUERY += ","

    for fkName in table['foreignKeys']:
        QUERY += "FOREIGN KEY(" + fkName + ") REFERENCES " + \
            table['foreignKeys'][fkName] + "(" + fkName + "),"
    # here we have to delete the last (,) in out query :)
    QUERY = QUERY[:-1]
    QUERY += ")"
    queries.append(QUERY)
    QUERY = ""

for query in queries:
    print(query)
    cur.execute(query)
db.close()
