from includes.database import *

def getTables(tables):
    return list(tables.keys())


def getTable(nameTable):
    return tables[nameTable]


def getAttributes(nameTable):
    return getTable(nameTable)['attributes']


def getPKeys(nameTable):
    return getTable(nameTable)['primaryKeys']


def getFKeys(nameTable):
    return getTable(nameTable)['foreignKeys']

'''
	* insBU - Date inscription de l'étudiant dans la bibliothèque
	* @param nomE (string)
	* @return dateInscripBU (string)
'''
def insBU(nomE):
	cur = db.cursor()
	cur.execute("SELECT dateInscripBU FROM Etudiant WHERE nomE = '" + nomE + "' LIMIT 1")
	getEtudiant = cur.fetchone()
	return getEtudiant[0]

'''
	* insCour - La liste des étudiants inscrits et date d'inscription dans cours
	* @param num_cours (integer)
	* @return (list)
'''
def insCour(num_cours):
	cur = db.cursor()
	cur.execute("SELECT nomE, prenomE, dateInsc FROM Inscrit\
		JOIN Etudiant ON Inscrit.num_etu = Etudiant.num_etu\
		WHERE num_cours = ?\
	", [num_cours])
	myList = cur.fetchall()
	return myList