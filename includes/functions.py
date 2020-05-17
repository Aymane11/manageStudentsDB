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
	* insBU - Date inscription de l'etudiant dans la bibliotheque
	* @param nomE (string)
	* @return dateInscripBU (string)
'''
def insBU(nomE):
	cur = db.cursor()
	cur.execute("SELECT dateInscripBU FROM Etudiant WHERE nomE = '" + nomE + "' LIMIT 1")
	getEtudiant = cur.fetchone()
	return getEtudiant[0]

'''
	* insCour - La liste des etudiants inscrits et date d'inscription dans cours
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

'''
	* resuEtu -  les resultats de l’etudiant
	* @param num_etu (integer)
	* @return (list)
'''
def resuEtu(num_etu):
	cur = db.cursor()

	cur.execute("SELECT DISTINCT nomE, prenomE, note, nomC, Resultat.num_cours\
	 	FROM Resultat\
		JOIN Etudiant ON Resultat.num_etu = Etudiant.num_etu\
		JOIN Cours ON Resultat.num_cours = Cours.num_cours\
		WHERE Resultat.num_etu = ?\
		;", [num_etu])
	myList = cur.fetchall()

	finalList = []
	for resultat in myList:
		# Getting the min, max, and avg of a cours
		cur.execute("SELECT DISTINCT min(note), max(note), avg(note)\
			FROM Resultat\
			WHERE\
			Resultat.num_cours = ?\
		;", [resultat[4]])
		minMaxAvgNote = cur.fetchone()

		currentList = []
		# transform tuple to a list
		for x in resultat:
			currentList.append(x)
		# Add min, max and avg of note
		for x in minMaxAvgNote:
			currentList.append(x)
		finalList.append(currentList)
	return finalList

'''
	* resultEchec - La liste des etudiants inscrits ayant une note<10 groupes par nom module
	* @param none
	* @return (list: nom, prenom, note ; la moyene classe)
'''
def resultEchec():
	cur = db.cursor()
	'''
	cur.execute("SELECT nomE,prenomE,note,AVG(note),nomC FROM Etudiant E,Inscrit I,Resultat R,Cours C \
				WHERE E.num_etu=I.num_etu AND \
				I.num_cours=C.num_cours AND \
				R.num_etu=E.num_etu AND \
				R.num_cours=C.num_cours AND \
				note<10 GROUP BY nomC;")
	'''
	cur.execute("SELECT nomC,nomE,prenomE,note FROM Etudiant E,Resultat R,Cours C \
				WHERE R.num_etu=E.num_etu AND \
				R.num_cours=C.num_cours AND \
				note<10 ORDER BY nomC;")
	myList = cur.fetchall()
	return myList

'''
	* insr - les noms des etudiants inscrits dans tous les modules
	* @param none
	* @return (list: nom, prenom)
'''
def insr():
	cur=db.cursor()
	cur.execute("SELECT nomE,prenomE FROM Etudiant E \
				WHERE NOT EXISTS (\
				SELECT * FROM Cours C WHERE NOT EXISTS (\
				SELECT * FROM Inscrit I \
				WHERE I.num_etu=E.num_etu AND\
				I.num_cours=C.num_cours))")
	myList = cur.fetchall()
	return myList

'''	
	* empLiv - les Noms des etudiants avec date retour , qui ont empruntes le livre pour code Nlivre
	* @param Nlivre (integer)
	* @return (list: nom, prenom,datePret,dateRetour)
'''
def empLiv(Nlivre):
	cur=db.cursor()
	cur.execute("SELECT nomE,prenomE,date(datePret),date(DateRetour) FROM Etudiant E,Pret P \
				WHERE E.num_etu=P.num_etu AND \
				Nlivre="+str(Nlivre)+" AND \
				date(DateRetour) IS NOT NULL")
	myList = cur.fetchall()
	return myList

'''
	* retard - La liste des etudiants n ayant pas encore rendus au moins un livre
	* @param none
	* @return (list: nom, prenom,titre)
'''
def retard():
	cur=db.cursor()
	cur.execute("SELECT nomE,prenomE,titre,date(DateRetourPrevue) \
				FROM Etudiant E,Pret P,Livre L \
				WHERE E.num_etu=P.num_etu AND \
				P.Nlivre=L.Nlivre AND\
				date(DateRetour) IS NULL")
	myList = cur.fetchall()
	return myList

'''
	* noEmp - les noms des livres empruntes par personne
	* @param none
	* @return (list: titre,nom, prenom)
'''
def noEmp():
	cur=db.cursor()
	cur.execute("SELECT nomE,prenomE,titre \
				FROM Etudiant E,Pret P,Livre L \
				WHERE E.num_etu=P.num_etu AND \
				P.Nlivre=L.Nlivre \
				ORDER BY nomE")
	myList = cur.fetchall()
	return myList

'''
	* ResultTot - Chaque classe le nom de la classe et la moyenne des notes 
	* obtenues par cours obtenue dans la classe.
	* 
	* @return void
'''
def resultTot():
	cur = db.cursor()

	data = '''
	SELECT DISTINCT nomClasse, nomC, AVG(note)
	FROM Classe
	JOIN Etudiant ON Etudiant.numClasse = Classe.numClasse
	JOIN Resultat ON Resultat.num_etu = Etudiant.num_etu
	JOIN Cours ON Resultat.num_cours = Cours.num_cours
	GROUP BY nomClasse, nomC
	ORDER BY nomClasse ASC, nomC ASC
	'''
	cur.execute(data)
	data = cur.fetchall()

	return data

'''
	* modifierNomCours - Changer le nom d'un cours
	* @param num_cours(int)
	* @param nomC(int): nouveau nom de cours
	* @return void
'''
def modifierNomCours(num_cours, nomC):
	cur = db.cursor()

	query = '''
	UPDATE Cours SET nomC = ? WHERE num_cours = ?
	'''
	cur.execute(query, [nomC, num_cours])
	db.commit()

'''
	* supprimerCours - Supprimer un cours
	* @param num_cours(int)
	* @return void
'''
def supprimerCours(num_cours):
	cur = db.cursor()

	# On doit supprimer tous les colunnes qu'ont on relation avec ce cours.
	queries = [
		'DELETE FROM Resultat WHERE num_cours = ?;',
		'DELETE FROM Inscrit WHERE num_cours = ?;',
		'DELETE FROM Charge WHERE num_cours = ?;',
		'DELETE FROM Cours WHERE num_cours = ?;',
	]

	for query in queries:
		cur.execute(query, [num_cours])
		db.commit()