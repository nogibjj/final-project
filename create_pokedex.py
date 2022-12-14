import sqlite3
import pandas as pd

#read csv
data = pd.read_csv(r'data/Pokemon_all_gen.csv')
df = pd.DataFrame(data)

#set up database connection
conn = None
conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()

#drop existing pokedex table
DROP_TABLE = "DROP TABLE pokedex"
cursor.execute(DROP_TABLE)

#create new pokedex table
CREATE_TABLE = """ CREATE TABLE pokedex (
                ID integer PRIMARY KEY, 
                Name text NOT NULL,
                Form text,
                Type1 text NOT NULL,
                Type2 text,
                Total integer NOT NULL,
                HP integer,
                Attack integer,
                Defense integer,
                Sp_Atk integer,
                Sp_Def integer,
                Speed integer,
                Generation integer
                );"""
cursor.execute(CREATE_TABLE)
conn.commit()

#add data to the table
df.to_sql('pokedex',conn, if_exists='replace', index=False)

#print out all data in the table
cursor.execute("SELECT * FROM pokedex")
print(cursor.fetchall())

conn.close()