import oracledb, os
import requests
import random
import streamlit as st
import pandas as pd
import plotly.express as px


class main:
    def dbConn():
        url = "http://192.168.161.201:7003/InventoryDetailBean/InventoryDetailService?WSDL"
        headers = {
            'Content-Type': 'text/xml; charset=utf-8'
        }
        username="ranjith"
        userpwd="ranjith2022"
        connection = oracledb.connect(user=username, password=userpwd,
                                    port = '1521',dsn='192.168.161.200/RMSDEV')
        print("connected")
        source_cursor = connection.cursor()
        chunk_size = 1000
        sql1="""select item, status from item_master where status= 'A' fetch first 20 rows only"""
        sql2="""select item, status from item_master where status= 'S' fetch first 50 rows only """
        sql3="""select item, status from item_master where status= 'W' fetch first 30 rows only"""
        source_cursor.execute(sql1)
        data_1=[]
        rows1 = source_cursor.fetchall()
        for row in rows1:
            # print(row)
            data_1.append(row)
        source_cursor.close()
        source_cursor = connection.cursor()
        source_cursor.execute(sql2)
        data_2=[]
        rows2 = source_cursor.fetchall()
        for row in rows2:
            # print(row)
            data_2.append(row)
        source_cursor = connection.cursor()
        source_cursor.execute(sql3)
        data_3=[]
        rows3 = source_cursor.fetchall()
        for row in rows3:
            # print(row)
            data_3.append(row)
        connection.close()

        return data_1, data_2, data_3
# main.dbConn()

# username="TSTDBUSR"
# userpwd = os.environ.get("W3lc0me123")
# host = "192.168.161.46"
# port = 1521
# service_name = "RMSDEV"

# username="ranjith"
# userpwd = os.environ.get("ranjith2022")
# host = "192.168.161.200"
# port = 1521
# service_name = "RMSDEV"

# dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'
# connection = oracledb.connect(dsn)