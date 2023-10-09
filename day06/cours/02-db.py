import sqlite3
import json

from __init__ import DATABASE, SCHEMA

import os
os.remove(DATABASE)

connection = sqlite3.connect(DATABASE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

with open(SCHEMA, 'r') as f:
    schema = f.read()

connection.executescript(schema)

query = "INSERT INTO whisky (name, country, region, degree, price) VALUES (?, ?, ?, ?, ?)"
# cursor.execute(query, ("Richou", "France"))

connection.commit()

print("HERE")
cursor.execute("SELECT * FROM whisky ")
rows = cursor.fetchall()
for row in rows:
    print(dict(row)) 


print("HERE2")

with open("lmdw.json", 'r', encoding='utf-8') as f:
    jsonObj = json.load(f)
    for obj in jsonObj:
        cursor.execute(query, (obj["name"], obj["country"], obj["region"], obj["degree"], obj["price"]))
        print("executed")
        print(obj["country"])
        print(obj["region"])
        print(obj["price"])
        print(obj["name"])
connection.commit()
