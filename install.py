from inc.DB import *


tables = {
	# Table Auteur
	"Auteur": { 
		'foreignKeys': {}, 
		'primaryKeys': [
			'NAuteur',
		], 
		'attributes': {
			'NAuteur': ['INTEGER'],
			'nomA': ['TEXT', 'NOT NULL'],
			'prenomA': ['TEXT', 'NOT NULL'],
			'nationaliteA': ['TEXT', 'NOT NULL'],
		}
	},

	# Table Livre
	"Livre": { 
		'foreignKeys': {}, 
		'primaryKeys': [
			'Nlivre'
		], 
		'attributes': {
			'Nlivre': ['INTEGER'],
			'num_ISBN': ['TEXT', 'NOT NULL'],
			'titre': ['TEXT', 'NOT NULL'],
			'nbPages': ['INTEGER', 'NOT NULL'],
			'anneeS': ['INTEGER', 'NOT NULL'],
			'prix': ['REAL', 'NOT NULL'],
		}
	},

	# Table Possede :)
	"Possede": { 
		'foreignKeys': {
			'Nlivre': 'Livre',
			'Nauteur': 'Auteur',
		}, 
		'primaryKeys': [
		], 
		'attributes': {
			'Nlivre': ['INTEGER', 'NOT NULL'],
			'Nauteur': ['INTEGER', 'NOT NULL'],
		}
	},
}

cur = db.cursor()


QUERY = ""
queries = []

for nameTable,table in tables.items():
	QUERY += "CREATE TABLE IF NOT EXISTS " + nameTable + " ("
	for attribute in table['attributes']:
	 	QUERY += attribute + " "
	 	for typeA in table['attributes'][attribute]:
	 		QUERY += typeA + " "
	 	if (attribute in table['primaryKeys']):
	 		QUERY += "PRIMARY KEY"
	 	QUERY += ","

	for fkName in table['foreignKeys']:
		QUERY += "FOREIGN KEY(" + fkName + ") REFERENCES " + table['foreignKeys'][fkName]  + "(" + fkName + "),"
	# here we have to delete the last (,) in out query :)
	QUERY = QUERY[:-1]
	QUERY += ")"
	queries.append(QUERY)
	QUERY = ""

for query in queries:
	# print(query)
	cur.execute(query)
# db.close()
