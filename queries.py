import psycopg2

try:
    conn = psycopg2.connect("dbname='meanTea' user='Austin' host='localhost'")
    db = conn.cursor()
except:
    print("I am unable to connect to the database")


def getAll(table):
    db.execute("SELECT * FROM {0}".format(table))
    out = db.fetchall()
    return out;

def getCategories(table, arr):
    items = []
    for item in arr:
        db.execute("SELECT * FROM {0} WHERE item_id = '{1}'".format(table, item[0]))
        categories = db.fetchall()
        item += (categories,)
        items.append(item)
    return items

def getWhere(table, col, val):
    db.execute("SELECT * FROM {0} WHERE {1} = {2}".format(table, col, val))
    out = db.fetchall()
    return out

def addOne(data):
    db.execute("INSERT INTO kittens(name, color) VALUES ('{0}', '{1}')".format(data['name'], data['color']))
    return '';
