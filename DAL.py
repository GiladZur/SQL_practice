import sqlite3
from datetime import date
import time

PATH = "C:\\Users\\Owner\\Desktop\\DEVOPS_COURSE\\SQL_practice\\"
FILENAME = "Inventory.db"
FILE = PATH + FILENAME

def set_sql_connection():
    """
    This function will create connection to a database, using sqlite3 module
    This function returns a Connection object 
    """
    try:
        con = sqlite3.connect(FILE)
        return con
    except OperationalError as e:
        print(str(e))    

def set_cursor(con):
    """
    This function will create a Cursor object, once a connection had been made using set_sql_connection
    IN: con
    TYPE: sqlite3.connect
    OUT: cur
    TYPE: sqlite3.connect.cursor
    """
    cur = con.cursor()
    return cur

def close_sql_connection(con):
    """
    This function will commit any changes to an open sql connection and closes it.
    IN: con
    TYPE: sqlite3.connect 
    """
    con.commit()
    con.close()
    
def get_items():
    """
    This function retrieves all users information from a database
    IN: 
    OUT: Values from DB as LIST of Dict
    Type: LIST
    """
    con = set_sql_connection() ## Creates connection
    cur = set_cursor(con) ## Creates Cursor
    query = "SELECT * FROM Inventory" ## SQL QUERY
    data = cur.execute(query).fetchall() ## EXECUTING SQL QUERY
    dct = sort_as_dict(cur, data)
    close_sql_connection(con) ## Closing connection
    return dct

def sort_as_dict(cur, data):
    """
    This function receives cur, data, where:
    1. cur will be used to retrieve columns
    2. data will be used to retrieve values
    This function will return a list of dictionary {columns:values}
    """
    ## List Comprehension
    columns = [desc[0] for desc in cur.description] ## GETTING COLUMNS NAMES FROM DB
    result = []
    for row in data:
        row = dict(zip(columns, row))
        result.append(row)     
    return result

def is_item_exist(item):
    con = set_sql_connection() ## Creates connection
    cur = set_cursor(con) ## Creates Cursor
    query = "SELECT * FROM `Inventory`" ## SQL QUERY
    data = cur.execute(query).fetchall() ## EXECUTING SQL QUERY
    close_sql_connection(con)
    for row in data:
        if row[1] == item:
            return True
    return False

def insert_item(item, category, quantity, price, date):
    """
    This function inserts a new user into an existing database, once validating that the user or email doesnt exist
    """
    con = set_sql_connection() ## Creates connection
    cur = set_cursor(con) ## Creates Cursor
    if not (is_item_exist(item)): ## is exist validation
        query = "INSERT INTO Inventory (`Item`,`Category`,`Quantity`,`Price`,`Date`) VALUES (?,?,?,?,?)" ## PREPARED STATEMENT
        cur.execute(query, (item, category, quantity, price,date)) ## PREPARED STATEMENT
        print(f"New item had been added with values of: {item, category, quantity, price, date}")
    else:
        print("Item already exists")
    close_sql_connection(con)