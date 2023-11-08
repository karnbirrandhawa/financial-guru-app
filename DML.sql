 
 -- ----------- TRANSACTIONS PAGE -------------- -- 

 -- get transactions to display on transactions.html
SELECT date, amount, description, Accounts.account_name, Budget_categories.category_name 
FROM Transactions
	INNER JOIN Accounts ON Transactions.account_id=Accounts.account_id
    INNER JOIN Budget_categories ON Transactions.category_id = Budget_categories.category_id
    ORDER BY date DESC
;

 -- add transaction in transactions.html
INSERT INTO Transactions (date, amount, description, account_id, category_id)
    VALUES (:date_input, :amount_input, :description_input,
            :account_id_input_from_dropdown_input, :category_id_input_from_dropdown_input
            )
;

 -- get account_id to populate dropdown in transactions.html
SELECT account_id, account_name 
    FROM Accounts
    ORDER BY account_name
;

 -- get budget_categories to populate dropdown in transactions.html
SELECT category_id, category_name 
    FROM Budget_categories
    ORDER BY category_name
;


 -- ----------- ACCOUNTS PAGE -------------- --

 -- get accounts to display on accounts.html
SELECT Accounts.account_id, account_name, SUM(Transactions.amount) AS account_balance 
	FROM Accounts
	INNER JOIN Transactions ON Accounts.account_id=Transactions.account_id 
    GROUP BY Accounts.account_id
;

 -- add accounts 
 INSERT INTO Accounts (account_name, account_number)
	VALUES (:account_name_input, :account_number_input)
;

 -- delete from accounts
 DELETE FROM Accounts
    WHERE account_id = (SELECT account_id
                            FROM Accounts
                            WHERE account_name = :account_name_input_from_dropdown)
;

 -- get accounts to populate dropdown in accounts.html
 SELECT account_id, account_name 
    FROM Accounts
    ORDER BY account_name
;

 
 -- ----------- BUDGET CATEGORIES PAGE -------------- -- 

 -- get budget categories to display on categories.html
SELECT * FROM Budget_categories
;

 -- add new category in categories.html
INSERT INTO Budget_categories (category_name, category_budget)
    VALUES (:category_name_input, :category_budget_input)
;

 -- ----------- HOUSEHOLD MEMBERS PAGE -------------- --

 -- get household members to display on household-members.html
SELECT * FROM Household_members
;

 -- add household members 
INSERT INTO Household_members (member_name)
	VALUES (:member_name_input)
;

 -- get household members to populate dropdown in household-members.html
SELECT member_id, member_name
    FROM Household_members
    ORDER BY member_id ASC
;

 -- update from household members
UPDATE Household_members
SET member_name = :member_name_update
    WHERE member_id = :member_id_update_from_dropdown_input
;

 -- ----------- HOUSEHOLD_MEMBERS_ACCOUNTS INTERSECTION TABLE QUERIES (M:M RELATIONSHIP) -------------- --

 -- get household members accounts intersection table to display
SELECT * FROM Household_members_accounts
;

 -- add to household members accounts intersection table
INSERT INTO Household_members_accounts (account_id, member_id)
	VALUES (:account_id_input, :member_id_input)
;

-- delete from household members accounts intersection table
DELETE FROM Household_members_accounts 
    WHERE account_id = :account_id_deletion
    AND member_id = :member_id_deletion
;