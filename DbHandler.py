import sqlite3
from resources import *

def table_exists():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    table = ('accounts',)
    query = "select name from sqlite_master where type = 'table' and name = ?"

    try:
        cursor.execute(query,table)
        nTables = len(cursor.fetchall())
        conn.close()
        return nTables == len(table)
    except Exception as e:
        print('table_exists err')
        print(e)
        conn.close()
        return False

def create_table():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.executescript(open(resource_path('assets/schema.sql'),'r').read())
    conn.close()

def insert_row(row):
    cols = row.keys()
    vals = ([row[i] for i in cols])

    query = "insert into 'accounts' (%s) values (%s)" % (','.join(cols), (','.join(['?']*len(cols))))
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute(query,vals)
        conn.commit()
    except Exception as e:
        print("error inserting row")
        print(e)
    conn.close()

def get_col_names():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = "pragma table_info('accounts')"
    try:
        cursor.execute(query)
        res = cursor.fetchall()
    except:
        res = []
    conn.close()
    return res

def get_accounts():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = "select * from 'accounts'"
    cursor.execute(query)
    vals = cursor.fetchall()
    conn.close()
    res = [{'account_name':v[1],'account_secret':v[2]} for v in vals]
    return res