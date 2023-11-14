
# karn testing git commit/push

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import config


app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# database connection info
app.config["MYSQL_HOST"] = config.MYSQL_HOST
app.config["MYSQL_USER"] = config.MYSQL_USER
app.config["MYSQL_PASSWORD"] = config.MYSQL_PASSWORD
app.config["MYSQL_DB"] = config.MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = config.MYSQL_CURSORCLASS

mysql = MySQL(app)


# Routes
@app.route("/")
def home():
    return redirect("/accounts")


# route for accounts page
@app.route("/accounts", methods=["POST", "GET"])
def accounts():

    # Grab accounts data so we send it to our template to display
    if request.method == "GET":

        query = "SELECT account_id AS id, \
                        account_name AS 'Account Name', \
                        account_number AS 'Account Number' \
                    FROM Accounts"

        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("accounts.j2", data=data)

    # insert an account into the Accounts entity
    if request.method == "POST":
        # fire off if user presses the Add Account button
        if request.form.get("Add_Account"):
            # grab user form inputs
            account_name_input = request.form["name"]
            account_number_input = request.form["number"]

            # account for null account number
            if account_number_input == "":
                query = "INSERT INTO Accounts (account_name) VALUES (%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (account_name_input))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO Accounts (account_name, account_number) \
                            VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (account_name_input, account_number_input))
                mysql.connection.commit()

            # redirect back to accounts page
            return redirect("/accounts")


@app.route("/delete_account", methods=["POST"])
def delete_account():

    if request.form.get("Delete_Account"):
        account_id_input = request.form["account"]
        query = "DELETE FROM Accounts WHERE account_id = %s;"
        cur = mysql.connection.cursor()
        cur.execute(query, (account_id_input))
        mysql.connection.commit()

    return redirect("/accounts")


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=3000, debug=True)
