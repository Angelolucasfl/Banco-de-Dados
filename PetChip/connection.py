import psycopg2
from dotenv import load_dotenv, find_dotenv
import os

def get_connection():
    load_dotenv(find_dotenv())

    hostname = os.getenv('HOSTNAME')
    database = os.getenv('DATABASE')
    username = os.getenv('USER')
    password = os.getenv('PASSWORD')
    port_id = os.getenv('PORT')

    try:
        con = psycopg2.connect (
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port_id
        )

        cur = con.cursor()


    except Exception as error:
        print(error) 

    return con, cur