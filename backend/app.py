import os
from flask import Flask, request, jsonify
import mysql.connector


class DBManager:
    def __init__(self, database='example', host="database", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def person(self, Firstname, Lastname):
        self.cursor.execute(f"INSERT INTO person (Firstname, Lastname) Values ('{Firstname}', '{Lastname}')")
        self.connection.commit()

    def get_persons(self):
        self.cursor.execute('SELECT PersonID, Firstname, Lastname FROM person')
        rec = []
        for c in self.cursor:
            rec.append({'PersonID':c[0], 'Firstname':c[1], 'Lastname':c[2]})
        return rec

server = Flask(__name__)
conn = DBManager(password_file='/run/secrets/db-password')


@server.route('/person', methods = ["POST"])
def add_person():
    data = request.form
    first_name = data['firstname']
    last_name = data['lastname']
    conn.person(first_name,last_name)
    return f"<H1> {first_name} has been added to the database ", 201


@server.route('/persons', methods = ["GET"])
def get_persons():
    return jsonify(conn.get_persons())

        
if __name__ == '__main__':   
    server.run()
