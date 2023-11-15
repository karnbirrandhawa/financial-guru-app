from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request


app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_randhawk"
# app.config["MYSQL_PASSWORD"] = "1528"
# app.config["MYSQL_DB"] = "cs340_randhawk"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_allmanlj"
app.config["MYSQL_PASSWORD"] = "gNVb2MTHnklD"
app.config["MYSQL_DB"] = "cs340_allmanlj"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# # database connection info
# app.config["MYSQL_HOST"] = config.MYSQL_HOST
# app.config["MYSQL_USER"] = config.MYSQL_USER
# app.config["MYSQL_PASSWORD"] = config.MYSQL_PASSWORD
# app.config["MYSQL_DB"] = config.MYSQL_DB
# app.config["MYSQL_CURSORCLASS"] = config.MYSQL_CURSORCLASS

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
                cur.execute(query, (account_name_input,))
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
        cur.execute(query, (account_id_input,))
        mysql.connection.commit()

    return redirect("/accounts")


# route for household-members page
@app.route("/household-members", methods=["POST", "GET"])
def members():

    # Grab member data so we send it to our template to display
    if request.method == "GET":

        query = "SELECT member_id AS 'id', member_name AS 'Member Name' FROM Household_members"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("household-members.j2", data=data)

    # insert a member into the Household_members entity
    # if request.method == "POST":
    #     # fire off if user presses the Add Member button
    #     if request.form.get("Add_Member"):
    #         # grab user form inputs
    #         member_name_input = request.form["name"]
    #
    #         # account for null member input
    #         if member_name_input == "":
    #             query = "INSERT INTO Household_members (member_name) VALUES (%s)"
    #             cur = mysql.connection.cursor()
    #             cur.execute(query, (member_name_input,))
    #             mysql.connection.commit()
    #
    #         # no null inputs
    #         else:
    #             query = "INSERT INTO Household_members (member_name) VALUES (%s)"
    #             cur = mysql.connection.cursor()
    #             cur.execute(query, (member_name_input,))
    #             mysql.connection.commit()
    #
    #         # redirect back to household-members page
    #         return redirect("/household-members")

# Listener
# change the port number if deploying on the flip servers
# app is displaying on http://flip2.engr.oregonstate.edu:50121 when on the VPN and using above credentials  
if __name__ == "__main__":
    app.run(port=50121, debug=True)
 