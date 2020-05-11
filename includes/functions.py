from includes.database import tables

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