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

db.close()