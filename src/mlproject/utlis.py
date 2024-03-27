import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import mysql.connector

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
passw=os.getenv('password')
db=os.getenv("db")




def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1931",
            db="college"
            )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex,sys)