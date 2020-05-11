# Imports
from includes.database import *
from includes.functions import *
import csv

# Db cursor
cur = db.cursor()

# Query
QUERY = ""

# Queries
queries = []

# Creating Queries
for nameTable in getTables(tables):
    QUERY += "CREATE TABLE IF NOT EXISTS " + nameTable + " ("
    for attribute in getAttributes(nameTable):
        QUERY += attribute + " "
        for typeA in getAttributes(nameTable)[attribute]:
            QUERY += typeA + " "
        if (attribute in getPKeys(nameTable)):
            QUERY += "PRIMARY KEY"
        QUERY += ","

    for fkName in getFKeys(nameTable):
        QUERY += "FOREIGN KEY(" + fkName + ") REFERENCES " + \
            getFKeys(nameTable)[fkName] + "(" + fkName + "),"
    QUERY = QUERY[:-1]
    QUERY += ")"
    queries.append(QUERY)
    QUERY = ""

# Executing queries
for query in queries:
    cur.execute(query)
db.commit()

# Insering DATA
for nameTable in getTables(tables):
    with open(DATA_PATH + '/'+nameTable+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            questionMarks = ""
            sql = "INSERT INTO "+nameTable+'('
            for attribute in getAttributes(nameTable):
            	questionMarks += "?,"
            	sql += attribute+","
            sql = sql[:-1]
            questionMarks = questionMarks[:-1]
            sql += ") VALUES (" + questionMarks + ")"
            cur.execute(sql, row)
    db.commit()
    
db.commit()

"""
#Modification de la structure de la base

#1-Augmenter la taille de la colonne nom de la table étudiant.
cur.execute("CREATE TABLE new_Etudiant ( \
    num_etu INTEGER NOT NULL PRIMARY KEY, \
    nomE VARCHAR(60) NOT NULL , \
    prenomE VARCHAR(50) NOT NULL , \
    date_naissance VARCHAR(50) NOT NULL , \
    ville VARCHAR(50) NOT NULL , \
    dateInscripBU VARCHAR(50) NOT NULL , \
    dateAbs VARCHAR(50) , \
    numClasse INTEGER NOT NULL , \
    FOREIGN KEY(numClasse) REFERENCES Classe(numClasse));")
cur.execute("INSERT INTO new_Etudiant SELECT * FROM Etudiant;")
cur.execute("PRAGMA foreign_keys = OFF;")
cur.execute("DROP TABLE Etudiant;")
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("ALTER TABLE new_Etudiant RENAME TO Etudiant;")
db.commit()
#2-Ajouter le champ email a la table étudiant.
cur.execute("ALTER TABLE etudiant ADD COLUMN email VARCHAR(100);")
db.commit()
#3-Ajouter la colonne adresse à la table adresse.
cur.execute("ALTER TABLE etudiant ADD COLUMN adresse VARCHAR(100);")
db.commit()
#4-Supprimer les contraintes de la table pret.
cur.execute("CREATE TABLE IF NOT EXISTS new_Pret ( \
    Npret INTEGER , \
    num_etu INTEGER , \
    Nlivre INTEGER , \
    datePret VARCHAR(50) , \
    dateRetour VARCHAR(50) , \
    DateRetourPrevue VARCHAR(50));")
cur.execute("INSERT INTO new_Pret SELECT * FROM Pret;")
cur.execute("PRAGMA foreign_keys = OFF;")
cur.execute("DROP TABLE Pret;")
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("ALTER TABLE new_Pret RENAME TO Pret;")
db.commit()
#5-Modifier la table pret en y ajoutant les contraintes suivantes :

#a. Npret est clé primaire
cur.execute("CREATE TABLE IF NOT EXISTS new_Pret ( \
    Npret INTEGER NOT NULL PRIMARY KEY, \
    num_etu INTEGER, \
    Nlivre INTEGER, \
    datePret VARCHAR(50), \
    dateRetour VARCHAR(50) , \
    DateRetourPrevue VARCHAR(50));")
cur.execute("INSERT INTO new_Pret SELECT * FROM Pret;")
cur.execute("PRAGMA foreign_keys = OFF;")
cur.execute("DROP TABLE Pret;")
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("ALTER TABLE new_Pret RENAME TO Pret;")
db.commit()
#b. num_etu est une clé étrangère
cur.execute("CREATE TABLE IF NOT EXISTS new_Pret ( \
    Npret INTEGER NOT NULL PRIMARY KEY, \
    num_etu INTEGER, \
    Nlivre INTEGER, \
    datePret VARCHAR(50), \
    dateRetour VARCHAR(50) , \
    DateRetourPrevue VARCHAR(50), \
    FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu));")
cur.execute("INSERT INTO new_Pret SELECT * FROM Pret;")
cur.execute("PRAGMA foreign_keys = OFF;")
cur.execute("DROP TABLE Pret;")
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("ALTER TABLE new_Pret RENAME TO Pret;")
db.commit()
#c. Nlivre est une clé étrangère fais référence à la table livre.
cur.execute("CREATE TABLE IF NOT EXISTS new_Pret ( \
    Npret INTEGER NOT NULL PRIMARY KEY, \
    num_etu INTEGER, \
    Nlivre INTEGER, \
    datePret VARCHAR(50), \
    dateRetour VARCHAR(50) , \
    DateRetourPrevue VARCHAR(50), \
    FOREIGN KEY(num_etu) REFERENCES Etudiant(num_etu), \
    FOREIGN KEY(Nlivre) REFERENCES Livre(Nlivre));")
cur.execute("INSERT INTO new_Pret SELECT * FROM Pret;")
cur.execute("PRAGMA foreign_keys = OFF;")
cur.execute("DROP TABLE Pret;")
cur.execute("PRAGMA foreign_keys = ON;")
cur.execute("ALTER TABLE new_Pret RENAME TO Pret;")
db.commit()
#6-Modifier la table livre en y ajoutant la colonne Nauteur et la contrainte indiquant que cette colonne est une clé étrangère.

#7-Supprimer la table possede.

#8-Ajouter une contrainte à la table livre qui assure que titre de livre est une valeur unique.

#9-Ajoute les champs langue et NbreExemplaires à la table livre.

#10-Ajouter la contrainte qui assure l’unicité du numISBN.

#11-Ajouter la contrainte qui spécifie que date_retour est >= date_pret.
"""

db.close()