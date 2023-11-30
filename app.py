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

        query = "SELECT member_id AS 'id', \
                        member_name AS 'Member Name' \
                    FROM Household_members \
                    ORDER BY member_id ASC"
        
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("household-members.j2", data=data)

   #  insert a member into the Household_members entity
    if request.method == "POST":
        # fire off if user presses the Add Member button
        if request.form.get("Add_Member"):
            # grab user form inputs
            member_name_input = request.form["name"]
    
            # account for null member input
            if member_name_input == "":
                query = "INSERT INTO Household_members (member_name) VALUES (%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (member_name_input,))
                mysql.connection.commit()
    
            # no null inputs
            else:
                query = "INSERT INTO Household_members (member_name) VALUES (%s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (member_name_input,))
                mysql.connection.commit()
    
            # redirect back to household-members page
            return redirect("/household-members")

@app.route("/edit-household-members/<int:member_id>", methods=["POST", "GET"])
def edit_household_members(member_id):

    if request.method == "GET":
        # mySQL query to grab the info of the member with our passed id
        query = "SELECT * FROM Household_members WHERE member_id = %s" % (member_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("edit-household-members.j2", data=data)

    if request.method == "POST":
        # fire off if user clicks the 'Update Member' button
        if request.form.get("Update_Member"):
            # grab user form inputs
            member_id = request.form["member_id"]
            member_name = request.form["member_name"]

            query = "UPDATE Household_members \
                        SET member_name = %s \
                        WHERE member_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (member_name, member_id))
            mysql.connection.commit()

            # redirect back to members page after we execute the update query
            return redirect("/household-members")


# route for transactions page
@app.route("/transactions", methods=["POST", "GET"])
def transactions():

    # Grab transactions data so we send it to our template to display
    if request.method == "GET":
        query1 = "SELECT transaction_id AS ID, date AS Date, description AS Description, \
                        Accounts.account_name AS 'Account Name', Budget_categories.category_name AS Category, \
                        CONCAT('$ ', FORMAT(amount, 2)) AS Amount \
                     FROM Transactions \
                 INNER JOIN Accounts ON Transactions.account_id=Accounts.account_id \
                 INNER JOIN Budget_categories ON Transactions.category_id = Budget_categories.category_id \
                 ORDER BY date DESC;"
        cur = mysql.connection.cursor()
        cur.execute(query1)
        data = cur.fetchall()

        query2 = "SELECT account_id, account_name \
                      FROM Accounts \
                  ORDER BY account_name;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        account_data = cur.fetchall()

        query3 = "SELECT category_id, category_name \
                      FROM Budget_categories \
                  ORDER BY category_name;"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        category_data = cur.fetchall()

        return render_template("transactions.j2", data=data, account_data=account_data, category_data=category_data)


# Listener
# change the port number if deploying on the flip servers
# app is displaying on http://flip2.engr.oregonstate.edu:50121 when on the VPN and using above credentials  
if __name__ == "__main__":
    app.run(port=50121, debug=True)
 