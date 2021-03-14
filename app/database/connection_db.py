import mysql.connector
from mysql.connector import Error
import peewee as pw

def create_connection_db(database,user, password, host, port): 
    myDB = pw.MySQLDatabase(database,user=user,passwd=password, host=host,port=port)
    return myDB
