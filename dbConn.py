import configparser
import oracledb, os
import requests
import random
import streamlit as st
import pandas as pd
import plotly.express as px
from configparser_crypt import ConfigParserCrypt
from cryptography.fernet import Fernet

class jsonConversion:
    #this array is ging to store the values from the functions, at the end of the function. it is getiting called and returned in the 
    #append_all_the_outputs()
    def __init__(self):
        # Initialize an empty list to store the results
        self.results_array = []

    def compiled_array_return(self):
        self.results_array = self.results_array
        return self.results_array


    def read_encrypted_config(self, filename):
        # Load the encrypted configuration from the file
        with open(filename, 'r') as encrypted_file:
            encrypted_config = encrypted_file.read()

        # # Load the secret key from the file
        # with open('secret.key', 'rb') as key_file:
        #     secret_key = key_file.read()
        # Load the secret key from the file
        with open('secret-trainingdb.key', 'rb') as key_file:
            secret_key = key_file.read()

        # Create a Fernet cipher using the loaded secret key
        cipher = Fernet(secret_key)

        # Decrypt the configuration string
        decrypted_config = cipher.decrypt(encrypted_config.encode()).decode()

        return decrypted_config

    def read_client_details(self, filename):
        # Read the decrypted configuration
        decrypted_config = self.read_encrypted_config(filename)

        # Parse the configuration as INI
        config_parser = configparser.ConfigParser()
        config_parser.read_string(decrypted_config)

        # # Access the client details from the [client_details] section
        # username = config_parser.get('client_details', 'username')
        # userpwd = config_parser.get('client_details', 'userpwd')
        # port = config_parser.get('client_details', 'port')
        # dsn = config_parser.get('client_details', 'dsn')

        # Access the client details from the [client_details] section
        username = config_parser.get('training_db', 'username')
        userpwd = config_parser.get('training_db', 'userpwd')
        port = config_parser.get('training_db', 'port')
        dsn = config_parser.get('training_db', 'dsn')

        return username, userpwd, port, dsn

    
class main:
    
    def dbConn():
        creds = jsonConversion()
        # filename = 'encrypted_client_details.ini'
        filename ='encrypted_training_db.ini'
        username, userpwd, port, dsn = creds.read_client_details(filename)
        connection = oracledb.connect(user=username, password=userpwd,
                                        port = port,dsn=dsn)
        
        source_cursor = connection.cursor()
        chunk_size = 1000

        # sql1="""select item, status from item_master where status= 'A' fetch first 20 rows only"""
        # sql2="""select item, status from item_master where status= 'S' fetch first 50 rows only """
        # sql3="""select item, status from item_master where status= 'W' fetch first 30 rows only"""
        # source_cursor.execute(sql1)
        # data_1=[]
        # rows1 = source_cursor.fetchall()
        # for row in rows1:
        #     # print(row)
        #     data_1.append(row)
        # source_cursor.close()
        # source_cursor = connection.cursor()
        # source_cursor.execute(sql2)
        # data_2=[]
        # rows2 = source_cursor.fetchall()
        # for row in rows2:
        #     # print(row)
        #     data_2.append(row)
        # source_cursor = connection.cursor()
        # source_cursor.execute(sql3)
        # data_3=[]
        # rows3 = source_cursor.fetchall()
        # for row in rows3:
        #     # print(row)
        #     data_3.append(row)

        sql4="SELECT order_id, ship_mode FROM ORDERS2 where segment in ('Consumer', 'Corporate') "
        source_cursor = connection.cursor()
        source_cursor.execute(sql4)
        data_4=[]
        rows3 = source_cursor.fetchall()

            # Create a DataFrame from the fetched rows
        df1 = pd.DataFrame(rows3, columns=['order_id', 'ship_mode'])
        
        # Write the DataFrame to an Excel file
        excel_file_path = 'output.xlsx'
        df1.to_excel(excel_file_path, index=False)  # Set index=False to exclude DataFrame index from Excel
        
        print(f"Data written to Excel file: {excel_file_path}")

        for row in rows3:
            # print(row)
            data_4.append(row)
        connection.close()
        #direct db data
        # return data_4
        return #for excel access
        
# main.dbConn()

