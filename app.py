# Sample Flask application for a BSG database, snapshot of BSG_people

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# database connection info
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "bsg_universe"
# app.config["MYSQL_DB"] = "financial_guru"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes
# have homepage route to /people by default for convenience, generally this will be your home route with its own template
@app.route("/")
def home():
    return redirect("/accounts")


# route for people page
@app.route("/accounts", methods=["POST", "GET"])
def people():

    # Grab bsg_people data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the people in bsg_people
        # query = "SELECT id, fname FROM bsg_people"
        # query = "SELECT * FROM bsg_planets"
        # query = "SELECT account_id, account_name FROM Accounts"
        query = "SELECT Accounts.account_id AS id, account_name AS 'Account Name', \
                    SUM(Transactions.amount) AS 'Account Balance' \
                    FROM Accounts \
                    INNER JOIN Transactions ON Accounts.account_id=Transactions.account_id \
                    GROUP BY Accounts.account_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        print(cur)
        print(data)
        return render_template("accounts.j2", data=data)


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=3000, debug=True)
