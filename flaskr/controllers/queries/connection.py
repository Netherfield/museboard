import mysql.connector as m
from mysql.connector.errors import Error
from typing import Any



def create_server_connection(host_name:str,
                             user_name:str,
                             user_password:str) \
                            -> m.connection.MySQLConnection:
    connection = None
    try:
        connection = m.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection:m.connection.MySQLConnection,
                    query:str) \
                    -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")



def create_db_connection(host_name:str,
                        user_name:str,
                        user_password:str,
                        db_name:str) \
                        -> m.connection.MySQLConnection:
    connection = None
    try:
        connection = m.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection:m.connection.MySQLConnection,
                  query:str) \
                -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def execute_insert(connection:m.connection.MySQLConnection,
                  insert:str,
                  data:list) \
                -> None:
    cursor = connection.cursor()
    try:
        cursor.executemany(insert, data)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection:m.connection.MySQLConnection,
               query:str) \
            -> None:
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")