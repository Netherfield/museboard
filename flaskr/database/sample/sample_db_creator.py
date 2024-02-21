import csv
from database.connection_manager import sqlite_connector, PATH_SQL

def create_sdb():
    """
    Execute 'queries.sql' script
    :return:
    """
    DB_NAME = input("Insert Db Name: ")
    with open("queries.sql") as file:
        conx, cursor = sqlite_connector(DB_NAME)
        cursor.executescript(file.read())
        conx.commit()
        conx.close()
    print("Done")

def insert_data_sdb():
    """
    Insert data into SQL DB -> Model: (Item_Name, Img_Link, Description, Description_Url, Short_Description, Item_Type)
    from: 'try.csv'
    :return:
    """
    try:
        with open("try.csv", "r", encoding="utf-8") as file:
            QUERY = """INSERT INTO items (Item_Name, Img_Link, Description, Description_Url, Short_Description, Item_Type)
            VALUES (?, ?, ?, ?, ?, ?);"""
            reader = csv.reader(file)
            conx, cursor = sqlite_connector(PATH_SQL)
            for x in reader:
                cursor.execute(QUERY, x)
            conx.commit()
            conx.close()
            print("Data inserted!")
    except Exception as e:
        print(f"errore: {e}")


