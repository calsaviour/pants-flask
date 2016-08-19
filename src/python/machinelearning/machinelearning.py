import pandas as pd
from sqlmanager import SqlHandler

sqlHandler = SqlHandler()

def hello():
    return "your beautiful"

if __name__=="__main__":
    print hello()
    sqlHandler.dropTable()
    sqlHandler.createTable()
    print pd.__version__
