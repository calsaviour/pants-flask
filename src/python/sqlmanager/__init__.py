import gsqlite3 as sqlite3

class SqlHandler(object):
    def __init__(self):
        self.connection = None

    def createTable(self):
        self.connection = sqlite3.connect("exampledb.db")
        # get a cursor object used to execute SQL commands
        cursor = self.connection.cursor()
        # create a table
        cursor.execute("""CREATE TABLE population
        (city TEXT, state TEXT, population INT)
        """)
        # close the database connection
        self.connection.close()

    def dropTable(self):
        self.connection = sqlite3.connect("exampledb.db")
        cursor = self.connection.cursor()
        cursor.execute("""DROP TABLE IF EXISTS population""")
        self.connection.close()

    def insertData(self):
        self.connection = sqlite3.connect("exampledb.db")
        cursor = self.connection.cursor()
        # insert data
        cursor.execute("INSERT INTO population VALUES('New York City', \ 'NY', 8200000)")
        cursor.execute("INSERT INTO population VALUES('San Francisco', \ 'CA', 800000)")
        # commit the changes
        conn.commit()
        # close the database connection
        self.connection.close()
