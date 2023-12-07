 
 -- ----------- TRANSACTIONS PAGE -------------- -- 

 -- get transactions to display on transactions.html
SELECT date AS Date, description AS Description,
            Accounts.account_name AS 'Account Name', Budget_categories.category_name AS Category,
            CONCAT('$ ', FORMAT(amount, 2)) AS Amount
        FROM Transactions
    INNER JOIN Accounts ON Transactions.account_id=Accounts.account_id
    INNER JOIN Budget_categories ON Transactions.category_id = Budget_categories.category_id
    ORDER BY date DESC
   ;

 -- add transaction in transactions.html
INSERT INTO Transactions (date, description, account_id, category_id, amount)
    VALUES (:date_input, :description_input, :account_id_input_from_dropdown_input,
            :category_id_input_from_dropdown_input, :amount_input
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
SELECT account_id AS id,
        account_name AS 'Account Name',
        account_number AS 'Account Number'
    FROM Accounts
;

 -- add accounts 
 INSERT INTO Accounts (account_name, account_number)
	VALUES (:account_name_input, :account_number_input)
;

 -- delete from accounts
 DELETE FROM Accounts
    WHERE account_id = :account_input_from_dropdown)
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
SELECT Accounts.account_name AS Account, Household_members.member_name AS Member
        FROM Household_members_accounts
    INNER JOIN Accounts ON Household_members_accounts.account_id=Accounts.account_id
    INNER JOIN Household_members ON
        Household_members_accounts.member_id = Household_members.member_id
;

 -- get accounts to populate dropdown
 SELECT account_id, account_name
        FROM Accounts
     ORDER BY account_name;

 -- add to household members accounts intersection table
INSERT INTO Household_members_accounts (account_id, member_id)
	VALUES (:account_id_input, :member_id_input)
;

-- delete from household members accounts intersection table
DELETE FROM Household_members_accounts 
    WHERE account_id = :account_id_deletion
    AND member_id = :member_id_deletion
;
