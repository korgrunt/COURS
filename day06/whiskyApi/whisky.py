import json
from flask import jsonify
import sqlite3

class Whisky:
    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        return

    def close_connection(self):
        self.connection.close()
        return

    def get_all(self): 
        result = self.cursor.execute('SELECT * FROM whisky').fetchall()
        data = [dict(row) for row in result]
        return jsonify(data)

    def get_one(self, id): 
        result = self.cursor.execute("SELECT * FROM whisky WHERE id = ?", (id,)).fetchone()
        if result:
            return dict(result)
        return "NOT FOUND"

    def create_one(self, name, country, region, degree, price): 
        result = self.cursor.execute("INSERT INTO whisky (name, country, degree, region, price) VALUES (?, ?, ?, ?, ?)", (name, country, degree, region, price))
        self.connection.commit()
        if result:
            return jsonify(dict(result))
        return "NOT FOUND"

    def update_one(self, id, name, country, region, degree, price): 
        result = self.cursor.execute("UPDATE whisky set name = ?, country = ?, degree = ?, region = ?, price = ? WHERE id = ?", (name, country, degree, region, price, id))
        self.connection.commit()
        return

    def patch_one(self, id, obj):
        initatial = self.get_one(id)
        print("TESTSTSTT")
        print(initatial.get('name'))
        print("TESTSTSTT")
        result = self.cursor.execute("UPDATE whisky set name = ?, country = ?, degree = ?, region = ?, price = ? WHERE id = ?", (obj.get('name',initatial.get('name')), obj.get('country', initatial.get('country')), obj.get('degree', initatial.get('degree')), obj.get('region', initatial.get('region')), obj.get('price', initatial.get('price')), id))
        self.connection.commit()
        return

    def delete_one(self, id):
        result = self.cursor.execute("DELETE FROM whisky WHERE id = ?", (id,))
        self.connection.commit()
        return



