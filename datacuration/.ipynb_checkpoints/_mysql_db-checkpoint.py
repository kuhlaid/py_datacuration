'''
This module handles MySQL database connections.
'''
import pymysql
from sqlalchemy import create_engine, update, insert, Table, Column, Numeric, Integer, String, MetaData
from sqlalchemy.engine import result

class MySql():
    def __init__(self,strMYSQL_USERNAME, strMYSQL_PASSWORD, strMYSQL_HOST, strMYSQL_DATABASE, intMYSQL_PORT):
        """
        Create the MySQL database connection strings needed to connect to the database when we are ready.
    
         Parameters
         ----------
         strMYSQL_USERNAME : str "Username to connect to MySQL."
         strMYSQL_PASSWORD : str "Password to connect to MySQL."
         strMYSQL_HOST : str "Username to connect to MySQL."
         strMYSQL_DATABASE : str "Name of database."
         intMYSQL_PORT : int "Database port number."
    
         Example
         ----------
         self.objDb = MySql("root", "someRidiculousPassword", "127.0.0.1", "sampledb", 3308)
        """
        self.blnHaveCon=False
        db_connection_str = "mysql+pymysql://"+strMYSQL_USERNAME+ ":" +strMYSQL_PASSWORD +"@"+strMYSQL_HOST+"/"+ strMYSQL_DATABASE
        self.db_engine = create_engine(db_connection_str, connect_args= dict(host=strMYSQL_HOST, port=intMYSQL_PORT))


    def checkDbConn(self):
        """
        Start a database connection. Try to create our database connection and ensure our database connection is working.
    
         Example
         ----------
         self.objDb.checkDbConn()
        """
        try:
            self.db_connection = self.db_engine.connect()
            if not self.blnHaveCon:
                print("It looks like our MySQL connection is good")
            self.blnHaveCon=True
            return True
        except:
            raise RuntimeError("***BLAHHHHH! We probably forgot to start our database server or port forward to it.***")
        return False


    def closeDbConn(self):
        """
        Close database connection. Do not call this directly.
        """
        self.db_connection.close()

    
    def disposeDb(self):
        """
        Dispose of database connection. Do not call this directly.
        """
        self.db_engine.dispose()

    
    def endDbConn(self):
        """
        Close and dispose of database connection.
    
         Example
         ----------
         self.objDb.endDbConn()
        """
        # https://stackoverflow.com/questions/8645250/how-to-close-sqlalchemy-connection-in-mysql
        self.closeDbConn()
        self.disposeDb()