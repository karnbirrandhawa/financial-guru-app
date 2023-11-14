
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

@app.route("/")
def home():
    return redirect("/accounts")


# route for accounts page
@app.route("/accounts", methods=["POST", "GET"])
def accounts():

    # Grab bsg_accounts data so we send it to our template to display
    if request.method == "GET":

        query = "SELECT Accounts.account_id AS id, account_name AS 'Account Name', \
                    SUM(Transactions.amount) AS 'Account Balance' \
                    FROM Accounts \
                    INNER JOIN Transactions ON Accounts.account_id=Transactions.account_id \
                    GROUP BY Accounts.account_id"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("accounts.j2", data=data)


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=3000, debug=True)
