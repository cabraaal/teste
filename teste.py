import pandas as pd
import streamlit as st
import psycopg2 as pg

conn = pg.connect(
    host= "localhost",
    database = "dsadb",
    user = "cabral",
    password = "ml05lc12",
    options="-c client_encoding=UTF8",
    port = "5434"

)

cursor = conn.cursor()
consulta = cursor.execute("SELECT * FROM cap03.estudantes_dsa;")
b = pd.DataFrame(cursor.fetchall())

st.dataframe(b)