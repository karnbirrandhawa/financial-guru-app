 
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
    VALUES (:date_input, :amount_input, :description_input, :account_id_input, :category_id_input)
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
                            WHERE account_name = :account_name_input)
;

 -- get accounts to populate dropdown in accounts.html
 SELECT account_id, account_name 
    FROM Accounts
    ORDER BY account_name
;
